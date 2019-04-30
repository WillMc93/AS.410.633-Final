from FASTA_utils import *

gene_path = "/home/will/Desktop/Final/FASTAs/Unknown Gene.fa"
rna_path = "/home/will/Desktop/Final/FASTAs/Unknown mRNA.fa"
promoter_path = "/home/will/Desktop/Final/FASTAs/Unknown Promoter.fa"
segment_path = "/home/will/Desktop/Final/FASTAs/UnknownGeneSegment.fa"

gene = fasta_read(gene_path)
rna = fasta_read(rna_path)
promoter = fasta_read(promoter_path)
segment = fasta_read(segment_path)

fasta_write(gene_path, gene, 'Unknown Gene')
fasta_write(rna_path, rna, 'Unknown RNA')
fasta_write(promoter_path, promoter, 'Unknown Promoter')
fasta_write(segment_path, segment, 'Unknown Gene Segment')

fasta_check(gene_path, gene)
fasta_check(rna_path, rna)
fasta_check(promoter_path, promoter)
fasta_check(segment_path, segment)