from FASTA_utils import fasta_read, fasta_write

gene_path = "/home/will/Desktop/Final/FASTAs/Unknown Gene.fa"

output_path = "/home/will/Desktop/Final/FASTAs/Exons/{}.fa"

exons = {1: (0, 510), 2: (1400, 1640), 3: (2298, 2538), 4: (2940, 3081), 5: (3671, 5121)}

gene = fasta_read(gene_path)

for i in range(1,6):
	exon = exons[i]
	a, b = exon
	exon = gene[a:b]

	print(len(exon))

	fasta_write(output_path.format(i), exon, "Exon {}".format(i))