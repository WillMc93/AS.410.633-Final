from FASTA_utils import fasta_read

template = "/home/will/Desktop/FASTAs/BLAST Results/AB071978-1(gene).fa"

given = "/home/will/Desktop/FASTAs/Unknown Gene.fa"

template = fasta_read(template)
given = fasta_read(given)