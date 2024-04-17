import argparse
import multiprocessing
from munge import generate_variants
import os

def process_password(password, level, verbose, output, index):
    temp_output = f"{output}_temp_{index}"
    generate_variants(password, level, verbose, temp_output)
    return temp_output

def merge_files(temp_files, final_output):
    with open(final_output, 'w') as outfile:
        for fname in temp_files:
            with open(fname) as infile:
                outfile.write(infile.read())
            os.remove(fname)  # Optionally remove the temp file after merging

def main():
    # Setup command line argument parsing
    parser = argparse.ArgumentParser(description="Password Variant Generator")
    parser.add_argument('-i', '--input', type=str, help="Input file with base passwords")
    parser.add_argument('-o', '--output', type=str, default="wordlist.txt", help="Output file for password variants")
    parser.add_argument('-l', '--level', type=int, choices=range(1, 6), default=1, help="Level of munging (1-5)")
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
        passwords = ['intruder']  # Default password list if no file provided

    # Setup multiprocessing
    pool = multiprocessing.Pool()
    jobs = []
    for index, password in enumerate(passwords):
        job = pool.apply_async(process_password, (password, args.level, args.verbose, args.output, index))
        jobs.append(job)
    results = [job.get() for job in jobs]
    pool.close()
    pool.join()

    # Merge all temporary files into the final output file
    merge_files(results, args.output)

    if args.verbose:
        print(f"All variants have been written to: {args.output}.")

if __name__ == "__main__":
    main()
