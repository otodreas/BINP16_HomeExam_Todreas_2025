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
motif = "at"


# Check for errors in variables


# Define functions
def find_motif(sequence, motif):
    """
    This function takes a sequence and a motif as arguments and returns a list
    containing all 1-based indices at which the motif can be found in the
    sequence.
    """
    pass


# Program logic
if __name__ == "__main__":
    # Get sequences.
    sequences_dict = read_file(input_file)
    print(sequences_dict)
