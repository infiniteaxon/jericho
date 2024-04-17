from colorama import Fore, Style, init
from itertools import product

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
number_patterns = ['69', '111', '222', '333', '420', '444', '555', '666', '777', '888', '999', '123', '321', '1234', '4321', '12345', '54321', '123456', '654321']
number_patterns += [str(x) for x in range(0, 33)]
number_patterns += [str(x) for x in range(1960, 2024)]
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+']

# Helper function to write variants to a file
def write_to_file(variants, output_file):
    with open(output_file, 'a') as file:
        for variant in sorted(set(variants)):
            file.write(f"{variant}\n")

def character_substitutions(password, output_file, verbose):
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
    for v in variants:
        for n in number_patterns:
            for c in special_chars:
                level_2.add(v + n)
                level_2.add(n + v)
                level_2.add(v + c)
                level_2.add(c + v)
                level_2.add(n + v + c)
                level_2.add(c + v + n)
                
    write_to_file(level_2, output_file)
    if verbose:
        print(f"Level 2 Variations: {len(level_2)}")
    return level_2

def level_3_patterns(variants, output_file, verbose):
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
                
    write_to_file(level_3, output_file)
    if verbose:
        print(f"Level 3 Variations: {len(level_3)}")
    return level_3

def level_4_patterns(variants, output_file, verbose):
    level_4 = set()
    for v in variants:
        for n in number_patterns:
            for c in special_chars:
                level_4.add(v + c + c)
                level_4.add(v + n + n)
                level_4.add(c + c + v)
                level_4.add(n + n + v)
                level_4.add(c + v + c + c)
                level_4.add(c + v + c + n)
                level_4.add(c + v + n + c)
                level_4.add(c + c + v + c + c)


    write_to_file(level_4, output_file)
    if verbose:
        print(f"Level 4 Variations: {len(level_4)}")
    return level_4

def level_5_patterns(variants, output_file, verbose):
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

    write_to_file(level_5, output_file)
    if verbose:
        print(f"Level 5 Variations: {len(level_5)}")
    return level_5

def generate_variants(password, level, verbose, output_file):
    # Starting with level 1 character substitutions
    variants = set()
    variants = character_substitutions(password, output_file, verbose)

    # Apply transformations based on the level
    if level >= 2:
        level_2_patterns(variants, output_file, verbose)
    if level >= 3:
        level_3_patterns(variants, output_file, verbose)
    if level >= 4:
        level_4_patterns(variants, output_file, verbose)
    if level == 5:
        level_5_patterns(variants, output_file, verbose)

    return variants
