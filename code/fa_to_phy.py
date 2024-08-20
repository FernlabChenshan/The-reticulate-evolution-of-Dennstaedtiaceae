#python fa_to_phy.py all.fa
import re
import sys

with open(sys.argv[1], 'r') as fin:
    sequences = [(m.group(1), ''.join(m.group(2).split()))
    for m in re.finditer(r'(?m)^>([^ \n]+)[^\n]*([^>]*)', fin.read())]
with open(sys.argv[2], 'w') as fout:
    fout.write('%d %d\n' % (len(sequences), len(sequences[0][1])))
    for item in sequences:
        fout.write('%-20s %s\n' % item)

