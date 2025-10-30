#!/usr/bin/env python3

"""
_helper.py (Question 2, Question 3, BINP16 home exam)

Description: Helper file containing a function used for both question 1 and
question 2.

User-defined functions:
    read_file(input_file: str, window_size: int): Read input file, return
sequences and corresponding lines in a dictionary.

Non-standard modules: none

The program addresses the following potential errors:
    - Excessively short sequence (shorter than the window size)
    - Invalid characters in sequences
    - No sequences in input file (tag '>' missing)

The program does not address the following potential errors:
    - Sequences split by newline characters

Inputs: none

Usage: imported

Version: 1.0
Date: 2025-10-31
Author: Oliver Todreas
"""

# Import libraries
import os
import sys


# Define function
def read_file(input_file: str, metric_len: int):
    """
    Read input file, append lines starting with '>' to the list sequences.
    Exit the program if a sequence is shorter than the window size or motif or
    if a sequence contains invalid characters. Break the loop once all lines
    have been read. If at least one sequence was found, return the dictionary
    of line numbers and sequences.
    """
    try:
        int(metric_len) # metric_len is a window size.
    except ValueError:
        metric_len = len(metric_len) # metric len is a motif.
    with open(input_file, "r") as f:
        i = 0
        sequences_dict = {}
        valid_characters = {"A", "C", "G", "T", "N", "-"}
        while True:
            i += 1  # Use counter to keep track of line number
            line = f.readline()
            if line.startswith(">"):
                sequence = line[1:].strip().upper()
                if len(sequence) < metric_len:
                    sys.exit(
                        f"Sequence on line {i} is shorter than the window size/motif length {metric_len}."
                    )

                # The union of the sequence characters and valid characters does not match the valid characters.
                if valid_characters != (valid_characters | set(sequence)):
                    sys.exit(f"Sequence on line {i} contains invalid characters.")
                sequences_dict[i] = sequence

            if not line:
                break

    if len(sequences_dict) == 0:
        sys.exit(f"No lines in '{input_file}' start with '>'. No sequences found.")
    else:
        return sequences_dict


def output_file_enumerator(output_file):
    """
    Look for filenames that have the same format as output_file. If found,
    append a suffix to output_file to avoid overwriting.
    """
    if os.path.isfile(output_file):
        sep = output_file.index(".")
        n_output_files = [
            f for f in os.listdir() if f.startswith(output_file[:sep])
        ]  # Find the number of files that match output_file (not including file extension).
        output_file = (
            output_file[:sep] + f"_{len(n_output_files) + 1}" + output_file[sep:]
        )  # Ensure suffix gets added before the extension.
    return output_file
