# FASTA Utilities, reading/writing

import re

def fasta_read(filename):
	with open(filename) as f:
		data = f.read()
		data = re.sub(r'[0-9]+', '', data)
		data = re.sub(r'\s', '', data)

def fasta_write(filename, data, id):
	with open(filename, 'w') as f:
		f.write('>{}'.format(id))

		i = 80
		while i < len(data):
			f.write(data[i:i+80] + '\n')
			i += 80