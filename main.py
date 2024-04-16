import argparse
from munge import generate_variants

def main():
    # Setup command line argument parsing
    parser = argparse.ArgumentParser(description="Password Variant Generator")
    parser.add_argument('-i', '--input', type=str, help="Input file with base passwords")
    parser.add_argument('-o', '--output', type=str, default="wordlist.txt", help="Output file for password variants")
    parser.add_argument('-l', '--level', type=int, choices=range(1, 5), default=1, help="Level of munging (1-4)")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose mode: display processing details")
    args = parser.parse_args()

    # Ensure the output file is empty before starting
    open(args.output, 'w').close()

    # Process passwords from the input file or use a default password if no file is provided
    if args.input:
        try:
            with open(args.input, 'r') as file:
                passwords = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: Input file {args.input} not found.")
            return
    else:
        passwords = ['password']  # Default password list if no file provided

    # Generate variants for each password
    for password in passwords:
        generate_variants(password, args.level, args.verbose, args.output)

    if args.verbose:
        print(f"All variants have been written to: {args.output}.")

if __name__ == "__main__":
    main()
