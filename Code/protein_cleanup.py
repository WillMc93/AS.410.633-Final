from FASTA_utils import *

protein_path = "/home/will/Desktop/Final/FASTAs/Protein.fa"

protein = fasta_read(protein_path)

protein = protein.replace('Met', 'M')

print(len(protein))

fasta_write(protein_path, protein, "Translated Protein")