#!/usr/bin/env python3

"""
2.py (Question 2, BINP16 home exam)

Description: Command line tool that takes input "2_input_Todreas.txt",
containing sequences in FASTA format, producing output "2_output_Todreas.txt",
containing GC content data within sliding windows of size 4. The variables
"input_file", "window_size", and "output_file" are hard coded for
reproducibility but can be changed

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

Usage: ./2.py

Version: 1.0
Date: 2025-10-31
Author: Oliver Todreas
"""

# Import libraries:
import sys
import os

from _helper import read_file


# Hard code inputs for reproducibility (user may change at their own discression)
input_file = "2_input_Todreas.txt"
window_size = 4
output_file = "2_output_Todreas.txt"


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
def gc_content(sequence: str, window_size: int):
    """
    Loop through the nucleotides in sequences, and count the number of G & C
    nucleotides in the reading frame. Based on GC counts, calculate and round
    GC percentage and append the value to the list gc_content_percentages.
    Return the list when the end of the loop is reached.
    """
    gc_content_percentages = []
    # Ensure that no subsequences shorter than the window size.
    for i in range(len(sequence) - window_size + 1):
        frame = sequence[i : i + window_size]
        gc_count = frame.count("G") + frame.count("C")
        gc_percent = round(gc_count / window_size * 100, 1)
        gc_content_percentages.append(gc_percent)

    return gc_content_percentages


def write_file(output_string: str, output_file: str):
    """
    Take the string output_string and append it to a file with the name
    output_file.
    """
    with open(output_file, "a") as f:
        f.write(output_string)


# Program logic
if __name__ == "__main__":
    # Get sequences.
    sequences_dict = read_file(input_file, window_size)
    # If the file output_file already exists, remove it to avoid appending lines to an already created file.
    if os.path.isfile(output_file):
        os.remove(output_file)

    for s in sequences_dict.values():  # Loop through sequences, write data to output_file.
        seq = f"Sequence: {s}\n"
        win = f"Window size: {window_size}\n"
        gc = f"GC content (%): {gc_content(s, window_size)}\n"
        output_string = seq + win + gc
        write_file(output_string, output_file)
