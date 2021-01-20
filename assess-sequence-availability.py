#!/usr/bin/python3

# Author: Joseph Sevigny
# Affiliation: Hubbard Center for Genome Studies, UNH
# Purpose: Automate the retrievel of genome reports from NCBI, taxonomy data from SILVA, and taxonomy from the barcode of life database.


import sys, re, argparse

# Parse the input files
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--input_list", help="simple of ncbi taxids")
parser.add_argument("--ncbi_taxonomy", help="expanded ncbi taxonomy database, the output from genbank_names_and_nodees_to_taxonomy.py'")
parser.add_argument("--output", help="output file with taxonomy added to the end, defult is input name.taxonomy.txt")
parser.add_argument("--taxid_field", help="field from input file that has the taxid, 0 based", type=int, default=0)

args = parser.parse_args()
input_list = args.input_list
taxid_to_taxonomy_file = args.ncbi_taxonomy
##

def taxidLookup(taxid_to_taxonomy_file):

    taxonomy_dictionary = {}  # tax_code:[taxonomy]

    for line in open(taxid_to_taxonomy_file, 'r'):
        elements = line.rstrip().split('\t')
        if len(elements) == 2:
            tax_id = elements[0]
            tax_info = elements[1].split(';')
            taxonomy_dictionary[tax_id] = tax_info
    return taxonomy_dictionary



taxonomy_lookup = taxidLookup(args.ncbi_taxonomy)
print ("Parsed taxonomy lookup")
# Parse files and provide taxonomy strings


with open(args.input_list + '.taxonomy.csv', 'w') as out_handle:
    for line in open(args.input_list):
        if line[0] != '#':
            taxid = line.rstrip().split('\t')[args.taxid_field]
            taxid = taxid.lstrip().rstrip() # remove any white spaces

            if taxid in taxonomy_lookup.keys():
                full_taxonomy = ','.join(taxonomy_lookup[taxid])
            else:
                full_taxonomy = 'FAILED_TO_LOCATE'
            out_handle.writelines(line.rstrip() + '\t' + full_taxonomy + '\n')
