#script for fixing copied and pasted flatfile sequences
import re
from sys import argv

file = argv[1]
identifier = ">" + argv[2] + "\n"
data = ""

with open(file) as f:
	data = f.read()
	data = re.sub("[0-9]+",'',data)
	data = re.sub("\s",'',data)

with open(file,'w') as f:
	f.write(identifier)

	i = 0
	while i < len(data):
		if len(data[i:]) > 80:
			f.write(data[i:i+80] + '\n')
			i += 80

		else:
			f.write(data[i:] + '\n')
			i = len(data)