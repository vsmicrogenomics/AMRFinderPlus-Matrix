# AMRFinderPlus-Matrix

AMRFinderPlus-Matrix.py
AMRFinderPlus-Matrix.py is a Python script for processing the output files of AMRFinderPlus and generating a binary matrix that shows the presence or absence of antibiotic resistance genes, stress response genes, and virulence genes in each sample.

Prerequisites
Python 3.7 or above
pandas library
Usage
Place the input files in a directory named input.
Run the script using the command python AMRFinderPlus-Matrix.py.
The binary matrix will be generated in a file named AMR_binary_matrix.tsv, STRESS_binary_matrix.tsv, and VIRULENCE_binary_matrix.tsv in the output directory.
Description
The script reads the input files from the input directory and processes each file to extract the relevant information for antibiotic resistance genes, stress response genes, and virulence genes. It then generates a binary matrix that shows the presence or absence of each gene in each sample.

The script defines a function process_file() that takes the file path and the element type as arguments. It reads the file into a pandas dataframe, filters the rows for the specified element type, selects only the relevant columns, and drops any duplicate rows.

The input and output directories are defined as input and output, respectively. The script loops over each element type (AMR, STRESS, VIRULENCE) and processes the files for that element type. The binary matrix for each element type is saved in a separate file in the output directory.

Test files
The test directory contains input and output sub-directories containing test files for the AMRFinderPlus-Matrix.py script. These files are used to verify that the script is working correctly.

Acknowledgements:
This script is based on the code snippets provided in the AMRFinderPlus documentation available at https://github.com/ncbi/amr/wiki/.

If you are using the `AMRFinderPlus-Matrix.py` script, please cite it as follows:
Sharma, V. (2023). AMRFinderPlus-Matrix.py [Python script]. Retrieved from https://github.com/vsmicrogenomics/AMRFinderPlus-Matrix


