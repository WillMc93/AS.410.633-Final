# removes the sequence in file2 from file1 and creates a new fasta file
from sys import argv

file1 = argv[0]
file2 = argv[1]
target = argv[2]

bigseq = ""
smallseq = ""

with open(file1):
	