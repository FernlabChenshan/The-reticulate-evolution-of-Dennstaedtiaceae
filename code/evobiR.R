#setwd("/Data02/xiazq/project/wanjue_geneflow_for_evobiR/folow_1/OrthoFinder/Results_Oct23/Single_Copy_Orthologue_Sequences/")
library(evobiR)
args <- commandArgs(trailingOnly = TRUE) 

CalcD(alignment = args[1], sig.test = "J", block.size = 10000, replicate = 100)
