# -*- coding: utf-8 -*-
# Date: 2022.9.18
# Author: Zengqiang Xia
# Function: Showing species counts for homologs filtering
# Usage: python3 get_taxa_number_from_seqs.py cluster.fa

import sys

species_list = []
with open (sys.argv[1], "r") as infile:
    for line in infile:
        if line[0] == '>':
            species = line.split("@")[0]
            if species not in species_list:
                species_list.append(species.strip())
print(sys.argv[1], len(species_list))


