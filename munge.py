from colorama import Fore, Style, init
import os

# Initialize Colorama
init(autoreset=True)

# Character substitutions focused on common leet speak and other transformations
substitutions = {
    'a': ['4', '@', '/\\'], 'b': ['8', '|3'], 'c': ['<', '(', '{'],
    'e': ['3', '&'], 'g': ['9', '6'], 'i': ['1', '!', '|'],
    'l': ['1', '|', '7'], 'o': ['0', '()'], 's': ['5', '$'],
    't': ['7', '+'], 'z': ['2'], 'h': ['#', '|-|'],
    'r': ['|2', '2'], 'd': ['|)', '(|'], 'n': ['^/', '|\\|'],
    'm': ['|\\/|', '/\\/\\'], 'u': ['|_|', '(_)'], 'v': ['\\/', '√'],
    'w': ['\\|/', '\\/\\/'], 'x': ['><', '×'], 'y': ['`/', '¥'],
    'p': ['|D', '|o'], 'q': ['O_', '9'], 'k': ['|<', '<|']
}

# Numerical patterns and special characters for enhancing password strength
number_patterns = ['666', '777', '888', '999', '1234', '4321', '12345', '54321']
number_patterns += [str(x) for x in range(0, 321)]
number_patterns += [str(x) for x in range(1960, 2024)]
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+']

# Helper function to write variants to a file
def write_to_file(variants, output_file):
    with open(output_file, 'a') as file:
        for variant in sorted(set(variants)):
            file.write(f"{variant}\n")

def character_substitutions(password, output_file, verbose):
    from itertools import product

    # Generate all possible substitutions
    def generate_all_combinations(pwd):
        options = []
        for char in pwd:
            substitutions_list = substitutions.get(char, [char])
            options.append([char] + substitutions_list)
        return set(''.join(comb) for comb in product(*options))

    substitutions_set = generate_all_combinations(password)
    write_to_file(substitutions_set, output_file)

    if verbose:
        print(f"Level 1 Variations: {len(substitutions_set)}")
    
    return substitutions_set

def level_2_patterns(variants, output_file, verbose):
    level_2 = set()
    for variant in variants:
        for number in number_patterns:
            level_2.add(variant + number)
            level_2.add(number + variant)
    write_to_file(level_2, output_file)
    if verbose:
        print(f"Level 2 Variations: {len(level_2)}")

def level_3_patterns(variants, output_file, verbose):
    level_3 = set()
    for variant in variants:
        for char in special_chars:
            level_3.add(char + variant)
            level_3.add(variant + char)
    write_to_file(level_3, output_file)
    if verbose:
        print(f"Level 3 Variations: {len(level_3)}")

def level_4_patterns(variants, output_file, verbose):
    level_4 = set()
    for variant in variants:
        for number in number_patterns:
            for char in special_chars:
                level_4.add(char + variant + number)
                level_4.add(number + char + variant)
                level_4.add(variant + number + char)
    write_to_file(level_4, output_file)
    if verbose:
        print(f"Level 4 Variations: {len(level_4)}")

def generate_variants(password, level, verbose, output_file):
    # Starting with level 1 character substitutions
    variants = character_substitutions(password, output_file, verbose)

    # Apply transformations based on the level
    if level >= 2:
        level_2_patterns(variants, output_file, verbose)
    if level >= 3:
        level_3_patterns(variants, output_file, verbose)
    if level == 4:
        level_4_patterns(variants, output_file, verbose)

    return variants