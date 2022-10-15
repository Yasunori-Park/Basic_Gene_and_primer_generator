from random import choices
import random
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

#Use ratio from Wikipedia page of Chargaff's rules:
#Homo Sapien: A = 29% G = 21% C = 20% T = 30%

def random_gene():
    url = "https://github.com/macarthur-lab/gene_lists/blob/master/lists/fda_approved_drug_targets.tsv"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    list = []
    find = soup.find_all(class_="pl-c1")
    for i in find:
        gene_name = i.string
        list.append(gene_name)
    random_gene = random.choice(list)
    return str(random_gene)

def random_mir():
    df = pd.ExcelFile('mir_list_ex.xlsx').parse('Sheet1')
    miR_list = df['list_mir'].tolist()
    random_miR = random.choice(miR_list)
    return str(random_miR)


def random_RTPCR_primer(number):
    DNA_bases = ['Ab', 'Tb', 'Cb', 'Gb']
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
    seq_with_space = ' '.join(seq[i:i+6] for i in range(0, len(seq), 6))
    seq_final = seq_with_space.replace('Ab', 'A').replace('Tb', 'T').replace('Cb', 'C').replace('Gb', 'G')
    seq_final_complement = seq_with_space.replace('Ab', 'T').replace('Tb', 'A').replace('Cb', 'G').replace('Gb', 'C')
    seq_final_reverse = str(seq_final)[::-1]
    seq_final_reverse_complement = str(seq_final_complement)[::-1]
    all_orientation = []
    all_orientation.extend((seq_final, seq_final_complement, seq_final_reverse, seq_final_reverse_complement))
    print("We amplified " + random_gene() + " that had a predicted binding site to " +
          random_mir() + " using the primer: " + str(all_orientation[0]))
    print("The COMPLEMENT of the primer is: " + all_orientation[1])
    print("The REVERSE of the primer is: " + all_orientation[2])
    print("The REVERSE COMPLEMENT of the primer is: " + all_orientation[3])

random_RTPCR_primer(20)
