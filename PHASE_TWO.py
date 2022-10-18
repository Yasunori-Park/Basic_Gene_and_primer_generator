from Bio import Entrez
from bs4 import BeautifulSoup
import sys
import random
import requests


Entrez.email = "yasunoripark@gmail.com"

url = "https://www.targetscan.org/cgi-bin/targetscan/vert_72/targetscan.cgi?species=Human&mir_sc=miR-145-5p"
url_miR = "hsa-miR-145-5p"


#Using the above targetscan url, choose a random gene to amplify.
def choose_gene():
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    gene_list = []
    for row in soup.find_all('td'):
        for columns in row.find_all('a', recursive=False):
            gene_list.append(columns.text)
    gene_list_trimmed = gene_list[4:]
    list_of_candidates = gene_list_trimmed[::3]
    choose_gene.var = str(random.choice(list_of_candidates))
    print("We are testing: "+ choose_gene.var)

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
    print("We amplified " + str(get_genbank_id.gene) + " " + str(get_genbank_id.var) +
          " which has a predicted binding site for " + str(url_miR) +
          " "+ str(get_ncbi_seq.var))

#Running the functions! :)
choose_gene()
get_genbank_id(choose_gene.var)
###Accession=get_genbank_id.var, start=200, primer_length=20, product=750, strand_1=1, strand_2=2
get_ncbi_seq(get_genbank_id.var, start=1500)
methodology_printout()
