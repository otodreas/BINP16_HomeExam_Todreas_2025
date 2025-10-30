#!/usr/bin/env python3

"""
_helper.py (Question 2, Question 3, BINP16 home exam)

Description: Helper file containing a function used for both question 1 and
question 2.

User-defined functions:
    read_file(input_file: str, window_size: int): Read input file, return
sequences.

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

# Define function
def read_file(input_file: str, window_size: int):
    """
    Read input file, append lines starting with '>' to the list sequences.
    Exit the program if a sequence is shorter than the window size or if a
    sequence contains invalid characters. Break the loop once all lines have
    been read. If at least one sequence was found, return the list sequences.
    """
    with open(input_file, "r") as f:
        i = 0
        sequences = []
        valid_characters = {"A", "C", "G", "T", "N", "-"}
        while True:
            i += 1  # Use counter to keep track of line number
            line = f.readline()
            if line.startswith(">"):
                sequence = line[1:].strip().upper()
                if len(sequence) < window_size:
                    sys.exit(
                        f"Sequence on line {i} is shorter than the window size {window_size}."
                    )

                # The union of the sequence characters and valid characters does not match the valid characters.
                if valid_characters != (valid_characters | set(sequence)):
                    sys.exit(f"Sequence on line {i} contains invalid characters.")
                sequences.append(sequence)

            if not line:
                break

    if len(sequences) == 0:
        sys.exit(f"No lines in '{input_file}' start with '>'. No sequences found.")
    else:
        return sequences