#!/usr/bin/env python3

"""
3.py (Question 3, BINP16 home exam)

Description: Command line tool that takes input "input_Todreas.txt",
containing sequences in FASTA format, producing outputs following the naming
convention "3_output_linex.png", where line x refers to the line in the input
file in which the sequence is found. The output file(s) are histograms plotting
the abundance of the motif "motif" across the sequence.

User-defined functions:
    find_motif(sequence, motif): Loop through a sequence, gather indices where
a given motif is found, return a list of hits as one-based indexes
    plotter(hits, input_file, motif, sequence_key, output_file): Generate
histograms of hits, set aesthetics using input_file, motif, and sequence_key,
and save the plot, ensuring good file naming.

Non-standard modules: matplotlib

Procedure:
    1. Import libraries
    2. Hard code inputs for reproducibility
    3. Check for input errors
    4. Define functions
    5. Run program

The program addresses the following potential errors:
    - Non-existent input file
    - Invalid motif (plots not saved if motif is not found)
    - Non-.png output file

Inputs: none

Usage: python3 ./3.py

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

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Please install matplotlib using 'pip install matplotlib'.")

from _helper import read_file, output_file_enumerator


# Get inputs, assign defaults
input_file = input("Enter input file name (Leave blank for reproducibility) ")
input_file = "input_Todreas.txt" if input_file == "" else input_file
motif = input("Enter motif (Leave blank for reproducibility) ")
motif = "at" if motif == "" else motif
output_file = input(
    "Enter output file naming template (Leave blank for reproducibility) "
)
output_file = "3_output_Todreas.png" if output_file == "" else output_file


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
    # Ensure that no subsequences shorter than the motif by subtracting the motif length from the range through which the loop iterates.
    for i in range(len(sequence) - len(motif) + 1):
        frame = sequence[i : i + len(motif)]
        if frame == motif.upper():
            hits.append(i + 1)

    return hits


def plotter(hits, input_file, motif, sequence_key, sequence_value, output_file):
    """
    Create a histogram of motif hits if there are any hits for a given
    sequence. Handle file naming inside function, ensuring that files do not
    get overwritten and instead get a suffix attached.
    """
    if len(hits) > 0:
        fig, ax = plt.subplots()
        # Create histogram. Assign bin count to the length of the sequence unless it is too long.
        ax.hist(hits, bins=len(sequence_value) if len(sequence_value) <= 20 else None)
        # Ensure the entire sequence is represented on the x axis, regardless of hits.
        ax.set_xlim(-0.5, len(sequence_value) - 0.5)
        # Since positions and number of hits are integers, force axes to be marked by integers.
        ax.set_xticks([int(xtick) for xtick in ax.get_xticks() if xtick % 1 == 0])
        ax.set_yticks([int(ytick) for ytick in ax.get_yticks() if ytick % 1 == 0])
        ax.set_xlabel("Position in sequence")
        ax.set_ylabel("Occurrence")
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
        print(
            f"Hits for motif {motif.upper()} in sequence on line {sequence_key} of file {input_file}: {hits}"
        )

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
        plotter(hits, input_file, motif, key, sequences_dict.get(key), output_file)
