#!/bin/bash

: '
TodreasQ1.sh

Description: This shell script generates a list of files with filenames that
match a pattern. It then sorts them, counts them, and tallys up the total
number of amino acids in all the files.

Usage: bash TodreasQ1.sh
You must run the script from the directory `root/scripts/answers/bash`
to ensure reproducibility.

Version: 1.0
Date: 2025-10-31
Author: Oliver Todreas
'

# Assign all files matching the template in the examples folder to FILES.
FILES=$(find ../../examples -name seq_*_chain*.fasta)

# Apply a sort to FILES. Note that since FILES contains relative file paths, directory names will affect the sort.
echo "Part 1: files matching the pattern seq_*_chain*.fasta sorted"
echo "$FILES" | sort

# Count the number of files in FILES.
echo "Part 2: number of files matching the pattern"
echo "$FILES" | wc -l

# Loop through FILES and count amino acids
echo "Part 3: total amino acids in files matching the pattern"

# Initiate total amino acid counter at 0
AMINO_ACIDS_TOTAL=0
for f in $FILES; do
    # Search for lines that do not start with ">" and count the number of characters in those lines.
    AMINO_ACIDS=$(grep -v "^>" $f | wc -m)
    
    # Use an arithmetic expression to update the total count of amino acids.
    AMINO_ACIDS_TOTAL=$(($AMINO_ACIDS_TOTAL + $AMINO_ACIDS))
done
echo $AMINO_ACIDS_TOTAL

# Make script executable to user.
chmod +x TodreasQ1.sh