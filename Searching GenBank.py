from Bio import Entrez
import sys
import random

Entrez.email = "yasunoripark@gmail.com"

#Function to retrieve the genbank ID for a gene of interest
def get_genbank_id(gene):
    term = "human[ORGN] " + str(gene) + "[GENE]"
    with Entrez.esearch(db="nucleotide",
                        term=term,
                        idtype="acc",
                        retmax="1") as handle:
        results = Entrez.read(handle)
        get_genbank_id.var = results["IdList"]
        get_genbank_id.gene = str(gene)

#Function to search GenBank using the ID from previous function
def get_ncbi_seq(accession, start=200, primer_length=20, product=750, strand_1=1, strand_2=2):
    #Parameters for your product length and primer lengths
    primer_length = int(primer_length)
    product = int(product)
    start= int(start)
    forward_primer_start = random.randrange(start)
    forward_primer_end = forward_primer_start + primer_length
    reverse_primer_end = forward_primer_start + product
    reverse_primer_start = reverse_primer_end - primer_length
    #Querying Entrez to search the nucleotide db for genes and bring back sequences matching above parameters
    try:
        #This generates the forward primer using strand=1.
        fetch_forward_primer = Entrez.efetch(
            db="nucleotide",
            rettype="fasta",
            retmode="text",
            id=accession,
            strand=strand_1,
            seq_start=forward_primer_start,
            seq_stop=forward_primer_end
        )
        #The reverse primer is generated using strand=2, meaning it is reverse complement to the accession FASTA.
        fetch_reverse_primer = Entrez.efetch(
            db="nucleotide",
            rettype="fasta",
            retmode="text",
            id=accession,
            strand=strand_2,
            seq_start=reverse_primer_start,
            seq_stop=reverse_primer_end
        )
        forward_primer = fetch_forward_primer.read()
        reverse_primer = fetch_reverse_primer.read()
        #For some reason primer length needs to be +3 to get the full generated "primer"
        primer_length_add_3 = primer_length + 3
        forward_primer_sequence_only = forward_primer[-primer_length_add_3:]
        reverse_primer_sequence_only = reverse_primer[-primer_length_add_3:]
        get_ncbi_seq.var = "with the forward RT-PCR primer: 5'-" + "".join(str(forward_primer_sequence_only).split()) + \
                             "-3'" + " and the reverse RT-PCR primer: 5'-" + "".join(str(reverse_primer_sequence_only).split()) + "-3'."
    except Exception:
        sys.stderr.write("Error! Cannot fetch: %s \n" % accession)

#Final output that would slot into the methodology
def methodology_printout():
    print("We amplified " + str(get_genbank_id.gene) + " " + str(get_genbank_id.var) + " "+ str(get_ncbi_seq.var))

#Running the functions! :)
get_genbank_id("FLI1")
###Accession=get_genbank_id.var, start=200, primer_length=20, product=750, strand_1=1, strand_2=2
get_ncbi_seq(get_genbank_id.var, start=1500)
methodology_printout()
