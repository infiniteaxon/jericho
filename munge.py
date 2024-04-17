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
            vn = variant + number
            level_2.add(vn)
            level_2.add(number + variant)
            level_2.add(number + vn)
    write_to_file(level_2, output_file)
    if verbose:
        print(f"Level 2 Variations: {len(level_2)}")
    return level_2

def level_3_patterns(variants, output_file, verbose):
    level_3 = set()
    for variant in variants:
        for char in special_chars:
            cv = char + variant
            cc = char + char
            level_3.add(cv)
            level_3.add(variant + char)
            level_3.add(cv + char)
            level_3.add(char + cv + cc)
            level_3.add(cv + cc)
            level_3.add(char + cv + char)
    write_to_file(level_3, output_file)
    if verbose:
        print(f"Level 3 Variations: {len(level_3)}")
    return level_3

def level_4_patterns(variants, output_file, verbose):
    level_4 = set()
    for variant in variants:
        for number in number_patterns:
            for char in special_chars:
                cvn = char + variant + number
                nc = number + char
                level_4.add(cvn)
                level_4.add(nc + variant)
                level_4.add(variant + nc)
                level_4.add(cvn + char)
                level_4.add(char + number + variant + nc)

    write_to_file(level_4, output_file)
    if verbose:
        print(f"Level 4 Variations: {len(level_4)}")
    return level_4

def level_5_patterns(variants, output_file, verbose):
    level_5 = set()
    for variant in variants:
        for number in number_patterns:
            for char in special_chars:
                cn = char + number
                nc = number + char
                cnc = cn + char
                ncn = nc + number
                level_5.add(variant + cnc)
                level_5.add(variant + ncn)
                level_5.add(cnc + variant)
                level_5.add(ncn + variant)
                level_5.add(cn + variant + cnc)
                level_5.add(nc + variant + cnc)
                level_5.add(cn + variant + ncn)
                level_5.add(nc + variant + ncn)
                level_5.add(cnc + variant + nc)
                level_5.add(cnc + variant + cn)
                level_5.add(ncn + variant + nc)
                level_5.add(ncn + variant + cn)
                level_5.add(cnc + variant + cnc)
                level_5.add(cnc + variant + ncn)
                level_5.add(ncn + variant + cnc)
                level_5.add(ncn + variant + ncn)

    write_to_file(level_5, output_file)
    if verbose:
        print(f"Level 5 Variations: {len(level_5)}")
    return level_5

def generate_variants(password, level, verbose, output_file):
    # Starting with level 1 character substitutions
    variants = set()
    level_2 = set()
    variants = character_substitutions(password, output_file, verbose)

    # Apply transformations based on the level
    if level >= 2:
        level_2 = level_2_patterns(variants, output_file, verbose)
        for variant in variants:
            level_2.add(variant)
    if level >= 3:
        level_3_patterns(level_2, output_file, verbose)
    if level >= 4:
        level_4_patterns(variants, output_file, verbose)
    if level == 5:
        level_5_patterns(variants, output_file, verbose)

    return variants
