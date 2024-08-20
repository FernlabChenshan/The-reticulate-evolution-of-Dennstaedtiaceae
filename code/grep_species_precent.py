# -*- coding: utf-8 -*-
# Date: 2022.10.27
# Author: Zengqiang Xia
# Function:Calculate the proportion of fasta file species
# Usage: python3 grep_species_precent.py OG123.fa
import sys
species_id = []
with open(sys.argv[1], "r") as fasta_file:
    for line in fasta_file.readlines():
        if line[0] == '>':
            gene_id = line.strip().split(".c")[0]    
            if gene_id not in species_id:
                species_id.append(gene_id)
#print (species_id) 
length = len(species_id)     
if length >= 10:
    print (sys.argv[1])
