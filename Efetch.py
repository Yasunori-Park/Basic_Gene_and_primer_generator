import sys
import pprint
import os
import pickle
import subprocess
import json
from pprint import pprint
from Bio import Entrez

def get_ncbi_seq(email, db, rettype, accession, strand, seq_start, seq_stop):

    # fetch
    print("Fetching accession %s from GenBank\n" % (accession))

    Entrez.email = email

    try:
        handle = Entrez.efetch(
            db=db,
            rettype=rettype,
            retmode="text",
            id=accession,
            strand=strand,
            seq_start=seq_start,
            seq_stop=seq_stop
        )
        res = handle.read()

        # for testing only
        # pickle_item(res, accession)
        print(res)
    except Exception:
        sys.stderr.write("Error! Cannot fetch: %s        \n" % accession)

#email, db, rettype, accession, strand, seq_start, seq_end
get_ncbi_seq("yasunoripark@gmail.com", "nuccore", "fasta", "NM_000314.8", "1", "20", "42")
