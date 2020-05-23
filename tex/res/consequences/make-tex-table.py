# Create tables for inclusion in .tex files

# This script loops over all consequences files

import json
import re
import pprint

# Populate files list
exec(compile(open("consequences.py", "r").read(), "consequences.py", 'exec'))
# The list named 'files' exists now!

pairs = {}

for file in files:
	with open(file, 'r') as f:
		content = json.load(f)
		left = file[:file.find('.json')]
		for right in content['right']:
			pairs[left + '-' + right] = [
				content['left'],
				content['argc'],
				content['right'][right]
			]

consequences = {}

for entry in pairs:
	content = pairs[entry]
	if content[1] == 1:
		msg = content[0].replace(' ...', '') + content[2][0].replace('...', '')
	elif content[1] == 2:
		msg = content[0]
		msg = re.sub(' \.\.\.', content[2][0].replace('...', ''), msg, 1)
		msg = re.sub(' \.\.\.', content[2][1].replace('...', ''), msg, 1)
	else:
		print("Warning: argc other than 1 or 2 encountered. Doing nothing.")
		break
	consequences[entry] = msg

pp = pprint.PrettyPrinter(indent = 4, width = 120)
pp.pprint(consequences)
