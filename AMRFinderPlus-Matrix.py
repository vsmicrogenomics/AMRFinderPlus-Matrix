#!/usr/bin/env python3

"""
AMRFinderPlus-Matrix.py

This script processes the output files of AMRFinderPlus and generates a binary matrix
that shows the presence or absence of antibiotic resistance genes, stress response
genes, and virulence genes in each sample.

Written by Vikas Sharma, 2023
"""

import pandas as pd
import os

# Define a function to process each input file
def process_file(file_path, element_type):
    # Read the file into a pandas dataframe
    df = pd.read_csv(file_path, sep='\t')
    # Filter the rows for the specified element type
    rows = df[df['Element type'] == element_type]
    # Select only the relevant columns and drop any duplicate rows
    return rows[['Gene symbol', 'Class', 'Subclass']].drop_duplicates(subset=['Gene symbol'])

# Define the input and output directories
input_directory = 'input'
output_directory = 'output'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the element types to process
element_types = {'AMR': 'AMR_binary_matrix.tsv',
                 'STRESS': 'STRESS_binary_matrix.tsv',
                 'VIRULENCE': 'VIRULENCE_binary_matrix.tsv'}

# Loop over each element type and process the files
for element_type, output_file_name in element_types.items():
    # Get a sorted list of all input files in the input directory
    input_files = sorted([os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith('.tsv')])

    # Initialize an empty dictionary to store the rows from all files
    rows_dict = {}

    # Loop over each input file and process it
    for file_path in input_files:
        # Extract the file name from the path
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        # Process the file and add the rows to the dictionary
        rows = process_file(file_path, element_type)
        rows_dict[file_name] = set(zip(rows['Gene symbol'], rows['Class'], rows['Subclass']))

    # Get a list of all unique combinations of Gene symbol, Class, and Subclass
    gene_class_subclass_set = set()
    for values_set in rows_dict.values():
        gene_class_subclass_set |= values_set
    gene_class_subclass_list = list(gene_class_subclass_set)

    # Create a list of dictionaries to store the binary matrix values
    binary_matrix_list = []
    for gene_class_subclass_tuple in gene_class_subclass_list:
        binary_dict = {'Gene symbol': gene_class_subclass_tuple[0],
                       'Class': gene_class_subclass_tuple[1],
                       'Subclass': gene_class_subclass_tuple[2]}
        for file_name in sorted(rows_dict.keys()):
            if gene_class_subclass_tuple in rows_dict[file_name]:
                binary_dict[file_name] = 1
            else:
                binary_dict[file_name] = 0
        binary_matrix_list.append(binary_dict)

    # Convert the list of dictionaries to a pandas dataframe and write it to the output file in TSV format
    binary_matrix_df = pd.DataFrame(binary_matrix_list)
    output_file = os.path.join(output_directory, output_file_name)
    binary_matrix_df.to_csv(output_file, sep='\t', index=False)
