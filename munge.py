from colorama import Fore, Style, init
import multiprocessing
from itertools import product

# Initialize Colorama
init(autoreset=True)

# Character substitutions focused on common leet speak and other transformations
substitutions = {
    'a': ['A', 'a', '4', '@'], 'b': ['B', 'b', '8'], 'c': ['C', 'c', '<', '('],
    'd': ['D', 'd', '|)'], 'e': ['E', 'e', '3', '&'], 'f': ['f', 'F'], 'g': ['G', 'g', '6'],
    'h': ['H', 'h', '#'], 'i': ['I', 'i', '1', '!', '|'], 'j': ['J', 'j'], 'k': ['K', 'k', '|<'],
    'l': ['L', 'l', '1', '|'],  'm': ['M', 'm'],  'n': ['N', 'n'],
    'o': ['O', 'o', '0', '()'], 'p': ['P', 'p'], 'q': ['Q', 'q', '9'], 'r': ['R', 'r'], 
    's': ['S', 's', '5', '$'], 't': ['T', 't', '7', '+'], 'u': ['U', 'u', '|_|', '(_)'], 'v': ['V', 'v'],
    'w': ['W', 'w'], 'x': ['X', 'x', '><'], 'y': ['Y', 'y'], 'z': ['Z', 'z', '2']
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

def level_2_patterns(v):
    level_2 = set()
    all_options = number_patterns + special_chars
    for n in number_patterns:
        for c in special_chars:
            level_2.add(v + n)
            level_2.add(n + v)
            level_2.add(v + c)
            level_2.add(c + v)
    for s in all_options:
        for t in all_options:
            level_2.add(v + s + t)
            level_2.add(s + v + t)
            level_2.add(s + t + v)
    return level_2

def level_3_patterns(v):
    level_3 = set()
    all_options = number_patterns + special_chars
    for s in all_options:
        for t in all_options:
            for f in all_options:
                level_3.add(v + s + t + f)
                level_3.add(s + v + t + f)
                level_3.add(s + t + v + f)
                level_3.add(s + t + f + v)
    return level_3

def level_4_patterns(v):
    level_4 = set()
    all_options = number_patterns + special_chars
    for s in all_options:
        for t in all_options:
            for f in all_options:
                for th in all_options:
                    level_4.add(v + s + t + f + th)
                    level_4.add(s + v + t + f + th)
                    level_4.add(s + t + v + f + th)
                    level_4.add(s + t + f + v + th)
                    level_4.add(s + t + f + th + v)
    return level_4


def level_5_patterns(v):
    level_5 = set()
    all_options = number_patterns + special_chars
    for s in all_options:
        for t in all_options:
            for f in all_options:
                for th in all_options:
                    for sth in all_options:
                        level_5.add(v + s + t + f + th + sth)
                        level_5.add(s + v + t + f + th + sth)
                        level_5.add(s + t + v + f + th + sth)
                        level_5.add(s + t + f + v + th + sth)
                        level_5.add(s + t + f + th + v + sth)
                        level_5.add(s + t + f + th + sth + v)
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
    final_variants = set(password)
    variants = character_substitutions(password)  # This should return a set of initial variants
    with multiprocessing.Pool(processes=6) as pool:
        # Process each variant through process_variant function using starmap
        results = pool.starmap(process_variant, [(variant, level) for variant in variants])
    for result in results:
        final_variants.update(result)

    return final_variants
