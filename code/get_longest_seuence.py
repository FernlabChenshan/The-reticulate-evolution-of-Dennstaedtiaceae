# -*- coding: utf-8 -*-
# Date: 2022.8.14
# Author: Zengqiang Xia
# Function:Extract the longest transcript
# Usage: python3 get_longest_sequence.py target.fa
"""
Example sequence:
>GENE_1.1
xzqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
>GENE_1.2
AAAAAAAAAAA
AAAAAA
>GENE_2.1
CCCCCCCCCCCCCCC
>GENE_2.2
xzqDDDDDDDDDDDDDDDDDDDDDD
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
"""
import sys
aid = []
uniq_aid = []
adict = {}
bdict = {}
cdict = {}
new_id = []
ddict = {}
infile = open(sys.argv[1], "r")
#outfile = open('temp.txt',"a")
for line in infile.readlines():
    if line[0] == '>':
        sequence_id = line[1:7]
        aid.append(sequence_id)
        uniq_aid = list(set(aid))
        key = line.strip()
        adict[key] = []
    else:
        adict[key].append(line.strip())
for key, value in adict.items():
    key2 = key
    bdict[key2] = "".join(value)
#print(bdict)
#print(uniq_aid)
for b_key, b_value in bdict.items():
    gene_id = b_key[1:7].strip()
    #print(gene_id)
    if gene_id not in new_id:
        new_id.append(gene_id)
        cdict[gene_id] = []
        cdict[gene_id].append(b_value.strip()) 
    else:
        cdict[gene_id].append(b_value.strip())
#print(cdict)
for c_key, c_value in cdict.items():
    for seq in cdict[c_key]:
        longest_seq = max(cdict[c_key], key=len).strip()
        if c_key not in ddict:
            d_key = c_key
            ddict[d_key] = longest_seq
#print(ddict)
for d_key, d_value in ddict.items():
    ID = ">" +  d_key + "\n"
    Seq = d_value.strip()
    ID_Seq = ID + Seq
    print(ID_Seq)
