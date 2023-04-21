# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:33:10 2023

@author: Dan
"""
from Bio import SeqIO
import re
import os

fasta_file_folder='fasta_folder'
fasta_delimiter='.fasta'

length_of_seq=80
regex='SSSSS'

output_file="polyserine_containing_proteins.faa"

completed_file_list=[]

seqnum=0
polyseqs=0
files=os.listdir(fasta_file_folder)
for filenum in list(range(0, len(files))):
     for seq in SeqIO.parse(os.path.join(fasta_file_folder, files[filenum]), 'fasta'):
        seqnum+=1
        if bool(re.search(regex, str(seq.seq)[:length_of_seq]))==True:
            polyseqs+=1
            if seqnum%1000==0:
                print("Identified " + str(polyseqs) + " polyserine containing proteins from " + str(seqnum) + " analysed sequences\nCurrent file: " + str(files[filenum]))
            with open(output_file, "a") as output_handle:
                 SeqIO.write([seq], output_handle, "fasta")
     f=open('Completed_files.txt','a')
     f.write(str(files[filenum]))
     f.close()
            
