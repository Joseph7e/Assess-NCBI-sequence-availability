# Assess-NCBI-sequence-availability
This repository contains scripts and bioinformatics workflows for various use cases of the NCBI taxonomy database and for the collection of various sequence database statistics.
  
A python script to automate this process is currently in development. It is currently implemented as a BASH workflow only.
  
# Dependencies
Python3 v3.4.3+   
modules: Biopython, argsparse

# Usage 
--phylogeny tree.newick
 
This workflow currently requires a reference tree for the visualization of database coverage. The names of the leaves must exactly match those in the NCBI taxonomy database and must be limited to an individual scientific rank.
 
# Methods
  
### Expand the NCBI taxonomy database to create a lookup table of taxids.
  Locate and download the latest NCBI taxonomy database.   
  You will need the names and nodes file to construct the expanded taxonomy lookup.  
  Link updated January, 2021  

```bash
#prepare workign directory
mkdir ~/assess-sequence_database
mkdir ncbi_taxonomy/ && cd ncbi_taxonomy/

# download the ncbi taxonomy dump files.
wget ftp://ftp.ncbi.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz
tar xvzf *.tar.gz

#Expand the taxonomic lineages into a simplified tsv lookup.
python3 genbank_nodes_and_names_to_taxonomy.py  names.dmp nodes.dmp
cd ../
```


### Gather counts of available sequences and taxonomy reports from various databases.
 The first few steps gather the necessary files for each sequence database of interest. There is a heavy utilization of taxids that will be linked to the taxonomy lookup table.
If NCBI updates the taxonomy database and not the sequence report files, some sequences may be overlooked (and vise versa). A 'taxids_failed.txt' file will be provided that showcase any missing data.
 
### Genome sequences
```bash
mkdir genome-report && cd genome-report
wget https://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_genbank.txt

# expand taxids to full taxonomy strings
python3 ../Assess-NCBI-sequence-availability/assess-sequence-availability.py --input_list assembly_summary_genbank.txt --ncbi_taxonomy ../ncbi_taxonomy/expanded_ncbi_taxonomy.tsv --taxid_field 6

# count the number of genomes/assembles for each phylum
awk -F',' '{print $4, $NF}' metazoa_genomes_w_taxonomy.txt | sort | uniq | awk '{print $1}' | sort | uniq -c
```
 
  
### Complete mitochondrial genomes
  
  See https://github.com/Joseph7e/Target-Enrichment-of-Metazoan-Mitochondrial-DNA-with-Hybridization-Capture-Probes
  
  
### COX1 barcode of life
 Data was obtained from the BOLD http://barcodinglife.org/index.php/datarelease (this database has 99% arthropods??)
 http://barcodinglife.org/index.php/TaxBrowser_Home. Lists the phyla.  
  
### ribosomal rRNA - SILVA

   SILVA provides comprehensive, quality checked and regularly updated datasets of aligned small (16S/18S, SSU) and large subunit (23S/28S, LSU) ribosomal RNA (rRNA) sequences for all three domains of life (Bacteria, Archaea and Eukarya). https://www.arb-silva.de/
  
  Since we are focused on animals we start by downloadig the taxonomy reports for eukaryotes. Note that the taxonomic strings are a mess. I am currently looking into a method to convert the strings to taxids and then to ncbi taxonomy. taxids in the silva database do not match ncbis taxids.
     
  ```bash
mkdir silva138 && cd silva138
# download 18S data
wget "https://www.arb-silva.de/fileadmin/silva_databases/release_138_1/Exports/taxonomy/taxmap_slv_ssu_ref_nr_138.1.txt.gz"
#download 28S data
wget "https://www.arb-silva.de/fileadmin/silva_databases/release_138_1/Exports/taxonomy/taxmap_slv_lsu_ref_nr_138.1.txt.gz"

gunzip *.gz
## Header of file: primaryAccession,start,stop,organism_name,taxid
  ```
  
#Interesting papers
https://pubmed.ncbi.nlm.nih.gov/31364707/


