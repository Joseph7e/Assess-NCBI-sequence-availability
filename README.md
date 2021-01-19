# Assess-NCBI-sequence-availability
This repository contains scripts and bioinformatics workflows for various use cases of the NCBI taxonomy database and the collection of various sequence databases.

### Required input files
This workflow currently requires a reference tree for the visualization of database coverage. The names of the leaves must exactly match those in the NCBI taxonomy database and must be limited to an individual scientific rank.


### Expand the NCBI taxonomy database to create a lookup table of taxids.


### Gather files for various databases that showcase sequence coverage. 
The first few steps gather the necessary files for each sequence database of interest. There is a heavy utilization of taxids that will be linked to the taxonomy lookup table.
If NCBI updates the taxonomy database and not the sequence report files, some sequences may be overlooked (and vise versa). A 'taxids_failed.txt' file will be provided that showcase any missing data.

### Genome sequences
Download the "GENOME_REPORT.txt" file from NCBI.



### Complete mitochondrial genomes


### COX1 barcode of life








