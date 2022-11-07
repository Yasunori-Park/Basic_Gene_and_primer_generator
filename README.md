# Basic_Gene_and_primer_generator

WIP: Extremely basic generator for selecting a gene and an lncRNA from a list, and generating a primer. This is done as a way to see the flaws in the current standard operating procedure of wrongly identified nucleotide sequences (https://www.protocols.io/view/seek-amp-blastn-standard-operating-procedure-q26g7b2k1lwz/v1)

This was also done just to observe how easy it would be to generate methods sections claiming to have conducted RT-PCR, whilst containing wrongly identified nucletide sequence reagents (see: PMID 35022248), and gain an estimate on how quickly purported "paper-mills" generate manuscripts. 

# Phases

✔**Phase 1: Randomly generate sequences using the suggested ratio from the Wikipedia page of Chargaff's rules for Homo sapiens with a random selection of genes + miRs. DONE**✔. 

✔**Phase 2: Using a randomly selected miR, find a gene with a binding site (via TargetScan), find the relevant gene on NCBI and retrieve a given number of bases from the provided DNA sequence**✔. 

Phase 3: Repeat Phase 2, but set stringent rules for primer generation e.g. Forward and Reverse within Tm 5C, controlled GC content etc. 
