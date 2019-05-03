from FASTA_utils import *

# local paths
gene_path = "/home/will/Desktop/Final/FASTAs/Unknown Gene.fa"
rna_path = "/home/will/Desktop/Final/FASTAs/Unknown mRNA.fa"
promoter_path = "/home/will/Desktop/Final/FASTAs/Unknown Promoter.fa"
protein_path = "/home/will/Desktop/Final/FASTAs/Protein.fa"

# get and clean sequence data
gene = fasta_read(gene_path)
rna = fasta_read(rna_path)
promoter = fasta_read(promoter_path)
protein = fasta_read(protein_path)

# write the sequence data
fasta_write(gene_path, gene, 'Unknown Gene')
fasta_write(rna_path, rna, 'Unknown RNA')
fasta_write(promoter_path, promoter, 'Unknown Promoter')
fasta_write(protein_path, protein, 'Translated Protein')

# check that initial read matches current read
fasta_check(gene_path, gene)
fasta_check(rna_path, rna)
fasta_check(promoter_path, promoter)