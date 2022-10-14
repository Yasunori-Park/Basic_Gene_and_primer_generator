from random import choices
import random

#Use ratio from Wikipedia page of Chargaff's rules:
#Homo Sapien: A = 29% G = 21% C = 20% T = 30%

def random_char(number):
    DNA_bases = ['A', 'T', 'C', 'G']
    Chargaff_prob = [0.29, 0.30, 0.20, 0.21]
    list_of_list_bases = []
    for x in range(number):
        Chargaff_base = choices(DNA_bases, Chargaff_prob)
        list_of_list_bases.append(Chargaff_base)
    seq = ""
    for base in list_of_list_bases:
        seq = seq + ""
        for b in base:
            seq = seq + str(b)
    seq_final = ' '.join(seq[i:i+3] for i in range(0, len(seq), 3))
    return str(seq_final)

def random_gene():
    gene_list = []
    Random_names = ["PTEN", "PRX1", "TSM07", "P52", "SAPILP", "WHS91"]
    gene_list.append(random.choice(Random_names))
    Random_lncRNA = ["miR-15b", "miR-145", "Circular RNA ROCK1", "circ_0006156", "miR-521"]
    gene_list.append(random.choice(Random_lncRNA))
    statement = ("Wild-type 3' UTR of " + gene_list[0] + " that contained a predicted " +
          gene_list[1] + " target site was amplified by PCR using: ")
    return statement

print(random_gene() + random_char(20))