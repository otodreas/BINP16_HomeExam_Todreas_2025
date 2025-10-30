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
Since the inputs are hard coded for reproducibility, this program must be run
from the correct directory. ENSURE that you have cd'd into the directory
`root/scripts/answers/python`. If not, you will have to change the inputs in
the inputs section.

Version: 1.0
Date: 2025-10-31
Author: Oliver Todreas
"""

# Import libraries:
import sys
import os

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Please install matplotlib using 'pip install matplotlib'.")

from _helper import read_file, output_file_enumerator


# Hard code inputs for reproducibility (user may change at their own discression)
input_file = "input_Todreas.txt"
motif = "at"
output_file = "3_output_Todreas.png"


# Check for errors in variables
if not os.path.isfile(input_file):
    sys.exit(f"Input file '{input_file}' does not exist.")


if not output_file.endswith(".png"):
    sys.exit("Output file must be of format .png.")


# Define functions
def find_motif(sequence, motif):
    """
    This function takes a sequence and a motif as arguments and returns a list
    containing all 1-based indices at which the motif can be found in the
    sequence.
    """
    hits = []
    for i in range(len(sequence) - len(motif) + 1):
        frame = sequence[i : i + len(motif)]
        if frame == motif.upper():
            hits.append(i + 1)

    return hits


def plotter(hits, input_file, motif, sequence_key, output_file):
    """
    Create a histogram of motif hits if there are any hits for a given
    sequence. Handle file naming inside function, ensuring that files do not
    get overwritten and instead get a suffix attached.
    """
    if len(hits) > 0:
        fig, ax = plt.subplots()
        ax.hist(hits)
        ax.set_yticks(
            [tick for tick in ax.get_yticks() if tick % 1 == 0]
        )  # Since there can only be an integer number of hits, force y axis to be marked by integers.
        ax.set_ylabel("Occurrence")
        ax.set_xlabel("Position in sequence")
        fig.suptitle(
            f"Occurrences of motif {motif.upper()} in DNA sequence\non line {sequence_key} of file {input_file}"
        )
        fig.tight_layout()

        # Add the line number for the sequence from the input file before appending a suffix for duplicate file handling using output_file_enumerator.
        sep = output_file.index(".")
        output_file = (
            output_file[:sep] + "_line" + str(sequence_key) + output_file[sep:]
        )
        output_file = output_file_enumerator(output_file)
        fig.savefig(output_file)

    # Do not save plot if there are 0 hits for motif in sequence.
    else:
        print(
            f"0 hits for the motif {motif.upper()} in sequence on line {sequence_key} of file {input_file}. No plot generated."
        )


# Program logic
if __name__ == "__main__":
    # Get sequences, check that the user is in the directory where the input file is stored.
    try:
        sequences_dict = read_file(input_file, motif)
    except FileNotFoundError:
        sys.exit(
            "File not found. Are you sure you're running this script from the folder 'root/scripts/answers/python'?"
        )

    # Loop through keys (line numbers) for each sequence in sequences_dict.
    for key in sequences_dict:
        hits = find_motif(
            sequences_dict.get(key), motif
        )  # Get hits with the dictionary key (sequence).
        plotter(hits, input_file, motif, key, output_file)
