#!/usr/bin/env python3

"""
2.py (Question 2, BINP16 home exam)

Description: Command line tool that takes input "input_Todreas.txt", containing
sequences in FASTA format, producing output "2_output_Todreas.txt", containing
GC content data within sliding windows of size 4. The variables "input_file",
"window_size", and "output_file" are hard coded for reproducibility but can be
changed.

User-defined functions:
    gc_content(sequence: str, window_size: int): Loop through a sequence,
generating GC percentages on a sliding window of size window_size, return a
list with all GC percentages generated.
    write_file(output_string: str, output_file: str): Append the string
output_string to the file output_file.

Non-standard modules: none

Procedure:
    1. Import libraries
    2. Hard code inputs for reproducibility
    3. Check for input errors
    4. Define functions
    5. Run program

The program addresses the following potential errors:
    - Non-existent input file
    - Non-integer or 0 window size
    - Non-.txt output file

Inputs: none

Usage: python3 ./2.py

When asked for inputs, please leave them blank (ie hit Enter) to ensure
reproducibility.

This program must be run from the correct directory. ENSURE that you have cd'd
into the directory `root/scripts/answers/python` when running. If not, you will
have to change the inputs in the inputs section.

Version: 1.0
Date: 2025-10-31
Author: Oliver Todreas
"""

# Import libraries
import sys
import os

from _helper import read_file, output_file_enumerator


# Get inputs, assign defaults
input_file = input("Enter input file name (Leave blank for reproducibility) ")
input_file = "input_Todreas.txt" if input_file == "" else input_file
window_size = input("Enter window size (Leave blank for reproducibility) ")
window_size = 5 if window_size == "" else window_size
output_file = input("Enter output file naming template (Leave for reproducibility) ")
output_file = "2_output_Todreas.txt" if output_file == "" else output_file


# Check for errors in variables
if not os.path.isfile(input_file):
    sys.exit(f"Input file '{input_file}' does not exist.")

try:  # Ensure window_size can be converted to a positive non-zero integer.
    window_size = abs(int(window_size))
    0 / window_size
except ValueError:
    sys.exit(f"Window size must be convertable to integer, not '{window_size}'.")
except ZeroDivisionError:
    sys.exit("Window size cannot be 0.")

if not output_file.endswith(".txt"):
    sys.exit("Output file must be of format .txt.")


# Define functions
def gc_content(sequence, window_size):
    """
    Loop through the nucleotides in sequences, and count the number of G & C
    nucleotides in the reading frame. Based on GC counts, calculate and round
    GC percentage and append the value to the list gc_content_percentages.
    Return the list when the end of the loop is reached.
    """
    gc_content_percentages = []
    # Ensure that no subsequences shorter than the window size by subtracting the window size from the range through which the loop iterates.
    for i in range(len(sequence) - window_size + 1):
        frame = sequence[i : i + window_size]
        gc_count = frame.count("G") + frame.count("C")
        gc_percent = round(gc_count / window_size * 100, 1)
        gc_content_percentages.append(gc_percent)

    return gc_content_percentages


def write_file(output_string, output_file):
    """
    Take the string output_string and append it to a file with the name
    output_file.
    """
    with open(output_file, "a") as f:
        f.write(output_string)


# Program logic
if __name__ == "__main__":
    # Get sequences, check that the user is in the directory where the input file is stored.
    try:
        sequences_dict = read_file(input_file, window_size)
    except FileNotFoundError:
        sys.exit(
            "File not found. Are you sure you're running this script from the folder 'root/scripts/answers/python'?"
        )

    output_file = output_file_enumerator(output_file)

    for (
        s
    ) in sequences_dict.values():  # Loop through sequences, write data to output_file.
        seq = f"Sequence: {s}\n"
        win = f"Window size: {window_size}\n"
        gc = f"GC content (%): {gc_content(s, window_size)}\n"
        output_string = seq + win + gc
        write_file(output_string, output_file)
