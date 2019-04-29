# FASTA Utilities, reading/writing

import re

def fasta_read(filename):
	with open(filename) as f:
		data = f.read() # get full contents
		data = re.sub(r'>[.]+\n', '', data) # kill identifier
		data = re.sub(r'[0-9]+|\s', '', data) # kill line numbers/whitespace
		return data

def fasta_write(filename, data, id, writemode='w'):
	with open(filename, writemode) as f:
		f.write('>{}\n'.format(id)) # add identifier

		# write 80 chars at a time for a nice file
		i = 0
		while i < len(data):
			f.write(data[i:i+80] + '\n')
			i += 80