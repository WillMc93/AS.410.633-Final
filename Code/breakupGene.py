# removes the sequence from small from big and makes a new FASTA with the difference
from sys import argv

def read(filename):
	data = ""
	with open(filename) as f:
		data = f.read()

		data = data.split('\n')

		data = ''.join(d for d in data[1:])
	
	return data

def write(filename, id, data):
	with open(filename, 'w') as f:
		f.write('>' + id + ':\n')

		i = 0

		while i < len(data):
			if len(data[i:]) > 80:
				f.write(data[i:i+80] + '\n')
				i += 80

			else:
				f.write(data[i:] + '\n')
				i = len(data)

big = argv[1]
small = argv[2]
target = argv[3]
target_id = argv[4]

big = read(big)
small = read(small)

assert (len(big) > len(small))
print(len(big), len(small))

outp = big.replace(small, '')
print(len(outp))

write(target, target_id, outp)

