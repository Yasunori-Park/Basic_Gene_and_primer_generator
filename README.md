# WIP_Basic_Gene_and_primer_generator

WIP: Extremely basic generator for selecting a gene and an lncRNA from a list, and randomly generating a primer using the suggested ratio from the Wikipedia page of Chargaff's rules for Homo sapiens.

This was done just to observe how easy it would be to generate methods sections claiming to have conducted RT-PCR, whilst containing wrongly identified nucletide sequence reagents (see: PMID 35022248). 

Phase 1: Randomly generate sequences with a random selection of genes + miRs. DONE. 

Phase 2: Randomly generate sequences with a randomly selected miR, and genes shown to have targeted binding to the miR (via TargetScan)

Phase 3: Using a randomly selected miR, find a gene with a binding site (via TargetScan), find the relevant gene on NCBI and retrieve a given numnber of bases from the provided DNA sequence. 

Phase 4: Repeat Phase 3, but set stringent rules for primer generation e.g. Forward and Reverse within Tm 5C, controlled GC content etc. 
