from FASTA_utils import *

protein_path = "/home/will/Desktop/Final/FASTAs/Protein.fa"

ig_path = "/home/will/Desktop/Final/FASTAs/ProteinSplit/ig.fa"
kinase_path = "/home/will/Desktop/Final/FASTAs/ProteinSplit/kinase.fa"

protein = fasta_read(protein_path)

ig = protein[:225]
kinase = protein[225:]

fasta_write(ig_path, ig, "Immunoglobulin V-Type Heavy")
fasta_write(kinase_path, kinase, "Serine/Threonine Kinase, catalytic domain")