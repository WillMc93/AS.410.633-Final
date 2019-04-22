import re

re.compile("[0-9]+")

file = "C:\\Users\\whm0004\\Google Drive\\FinalProject\\Fcamr gene - AB071978"

data = ""

with open(file) as f:
    data = f.read()
    data = re.sub("[0-9]+", '', data)
    data = re.sub("\s", '', data)

with open(file, 'w') as f:
    f.write(">AB071978\n")
    f.write(data)
