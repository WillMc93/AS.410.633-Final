from FASTA_utils import fasta_read, fasta_write

gene_path = "/home/will/Desktop/Final/FASTAs/Unknown Gene.fa"
rna_path = "/home/will/Desktop/Final/FASTAs/Unknown mRNA.fa"
promoter_path = "/home/will/Desktop/Final/FASTAs/Unknown Promoter.fa"

#gene = fasta_read(gene_path)
rna = fasta_read(rna_path)
#promoter = fasta_read(promoter_path)

#fasta_write(gene_path, gene, 'Unknown Gene')
fasta_write(rna_path, rna, 'Unknown RNA')
#fasta_write(promoter_path, promoter, 'Unknown Promoter')