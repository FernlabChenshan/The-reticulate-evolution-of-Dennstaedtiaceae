# -*- coding: utf-8 -*-
# Date: 2022.9.4
# Author: Zengqiang Xia
# Function:Split the simulated gene tree into a single file
# Usage: python3 split_genetree.py all_genetree.txt
import sys
with open(sys.argv[1], "r") as infile:
    number = 0
    for line in infile:
        lines = line.strip()
        number += 1
        name = "genetree" + "_" + str(number) + ".tree"
        outfile = open(name, "w")
        outfile.write(lines)
        outfile.close()
