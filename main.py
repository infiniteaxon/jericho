import argparse
from munge import generate_variants
import os

def process_passwords(passwords, level):
    for password in passwords:
        variants = generate_variants(password, level)
        return variants

def main():
    parser = argparse.ArgumentParser(description="Password Variant Generator")
    parser.add_argument('-i', '--input', type=str, help="Input file with base passwords")
    parser.add_argument('-o', '--output', type=str, default="wordlist.txt", help="Output file for password variants")
    parser.add_argument('-l', '--level', type=int, choices=range(1, 6), default=1, help="Level of munging (1-5)")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Input file {args.input} not found.")
        return

    with open(args.input, 'r') as file:
        passwords = [line.strip() for line in file if line.strip()]

    with open(args.output, 'w') as outfile:
        variants = process_passwords(passwords, args.level)
        print(f"[+] Variations:", len(variants))
        for variant in sorted(variants):
            outfile.write(f"{variant}\n")

if __name__ == "__main__":
    main()
