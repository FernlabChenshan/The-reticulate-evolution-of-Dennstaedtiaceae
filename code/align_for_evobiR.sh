#!/bin/bash  
  
# Set working dir  
# cd /path/to/your/fasta/files  
  
# Set output dir 
mkdir -p aligned fasta  
  
# Run MAFFT 
echo "Generating MAFFT alignment commands..."  
for fa in *.fa; do  
    echo "mafft --auto $fa > aligned/${fa%.fa}.aligned" >> mafft.cmd.sh  
done  
  
echo "Running MAFFT alignments..."  
ParaFly -c mafft.cmd.sh -shuffle -CPU 10 -failed_cmds mafft.cmd.failed -v  
  
# sort sequences as P1 P2 P3 O 
echo "Sorting and merging alignments..."  
for aligned in aligned/*.aligned; do  
    seqkit sort "$aligned" | seqkit seq -w 0 >> flow_.fa  
done  
mv *.fa fasta  
echo "Processing completed."
