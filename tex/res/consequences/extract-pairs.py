# Create a newline-separated list of all entry names

# This script loops over all consequences files

import json

# Populate files list
exec(compile(open("consequences.py", "r").read(), "consequences.py", 'exec'))
# The list named 'files' exists now!

pairs = []

for file in files:
	with open(file, 'r') as f:
		content = json.load(f)
		left = file[:file.find('.json')]
		for right in content['right']:
			pairs.append(left+'-'+right)

output = ''
pairs.sort()
for pair in pairs:
	output = output + pair + '\n'

with open('./pairs.txt' , 'w') as f:
	f.write(output)
