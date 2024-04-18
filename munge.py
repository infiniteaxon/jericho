from colorama import Fore, Style, init
import multiprocessing
from itertools import product

# Initialize Colorama
init(autoreset=True)

# Character substitutions focused on common leet speak and other transformations
substitutions = {
    'a': ['A', 'a', '4', '@', '/\\'], 'b': ['B', 'b', '8', '|3'], 'c': ['C', 'c', '<', '(', '{'],
    'd': ['D', 'd', '|)', '(|'], 'e': ['E', 'e', '3', '&'], 'f': ['f', 'F'], 'g': ['G', 'g', '9', '6'],
    'h': ['H', 'h', '#', '|-|'], 'i': ['I', 'i', '1', '!', '|'], 'j': ['J', 'j'], 'k': ['K', 'k', '|<', '<|'],
    'l': ['L', 'l', '1', '|', '7'],  'm': ['M', 'm', '|\\/|', '/\\/\\'],  'n': ['N', 'n', '^/', '|\\|'],
    'o': ['O', 'o', '0', '()'], 'p': ['P', 'p', '|D', '|o'], 'q': ['Q', 'q', 'O_', '9'], 'r': ['R', 'r', '|2', '2'], 
    's': ['S', 's', '5', '$'], 't': ['T', 't', '7', '+'], 'u': ['U', 'u', '|_|', '(_)'], 'v': ['V', 'v', '\\/'],
    'w': ['W', 'w', '\\|/', '\\/\\/'], 'x': ['X', 'x', '><'], 'y': ['Y', 'y', '`/'], 'z': ['Z', 'z', '2']
}

# Numerical patterns and special characters for enhancing password strength
number_patterns = [str(x) for x in range(0, 10)]
# number_patterns += [str(x) for x in range(1990, 2024)]
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+']

def generate_all_combinations(pwd):
    options = []
    for char in pwd:
        substitutions_list = substitutions.get(char, [char])
        options.append(substitutions_list)
    return [''.join(combo) for combo in product(*options)]

def character_substitutions(password):
    return set(generate_all_combinations(password))

def level_2_patterns(variants):
    level_2 = set()
    for v in variants:
        for n in number_patterns:
            for c in special_chars:
                level_2.add(v + n)
                level_2.add(n + v)
                level_2.add(v + c)
                level_2.add(c + v)
                level_2.add(n + v + c)
                level_2.add(c + v + n)
    return level_2

def level_3_patterns(variants):
    level_3 = set()
    for v in variants:
        for n in number_patterns:
            for c in special_chars:
                level_3.add(v + n + c)
                level_3.add(v + c + n)
                level_3.add(n + c + v)
                level_3.add(c + n + v)
                level_3.add(v + n + c + c)
                level_3.add(v + c + n + c)
                level_3.add(n + c + v + c)
                level_3.add(c + n + v + c)
    return level_3

def level_4_patterns(variants):
    level_4 = set()
    for v in variants:
        for n in number_patterns:
            for c in special_chars:
                level_4.add(v + c + c)
                level_4.add(v + n + n)
                level_4.add(c + c + v)
                level_4.add(n + n + v)
                level_4.add(v + n + n + n)
                level_4.add(c + v + c + c)
                level_4.add(c + v + c + n)
                level_4.add(c + v + n + c)
                level_4.add(v + c + n + n + n)
                level_4.add(v + c + n + n + n + c)
    return level_4

def level_5_patterns(variants):
    level_5 = set()
    for v in variants:
        for n in number_patterns:
            for c in special_chars:
                level_5.add(v + c + n + c)
                level_5.add(v + n + c + n)
                level_5.add(c + n + c + v)
                level_5.add(n + c + n + v)
                level_5.add(c + n + v + c + n + c)
                level_5.add(n + c + v + c + n + c)
                level_5.add(c + n + v + n + c + n)
                level_5.add(n + c + v + n + c + n)
                level_5.add(c + n + c + v + n + c)
                level_5.add(c + n + c + v + c + n)
                level_5.add(n + c + n + v + n + c)
                level_5.add(n + c + n + v + c + n)
                level_5.add(c + n + c + v + c + n + c)
                level_5.add(c + n + c + v + n + c + n)
                level_5.add(n + c + n + v + c + n + c)
                level_5.add(n + c + n + v + n + c + n)
    return level_5

def process_variant(variant, level):
    final_variants = set()
    final_variants.add(variant)
    if level >= 2:
        final_variants.update(level_2_patterns(variant))
    if level >= 3:
        final_variants.update(level_3_patterns(variant))
    if level >= 4:
        final_variants.update(level_4_patterns(variant))
    if level == 5:
        final_variants.update(level_5_patterns(variant))
    return final_variants

def generate_variants(password, level):  
    variants = character_substitutions(password)  # This should return a set of initial variants
    with multiprocessing.Pool() as pool:
        # Process each variant through process_variant function using starmap
        results = pool.starmap(process_variant, [(variant, level) for variant in variants])

    # Create a set to collect all final variants
    final_variants = set()
    for result in results:
        final_variants.update(result)  # Assuming each result is a set of variants

    return final_variants
