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
		# Get starts of ' ...' and '...'
		loffset = content[0].find(' ...')
		roffset = content[2][0].find('...') + len('...')
		msg = content[0][:loffset] + content[2][0][roffset:]
	elif content[1] == 2:
		# Get starts of ' ...' and '...'
		offset = 0
		loffset = []
		roffset = []
		for match in re.finditer(' \.\.\.', content[0]):
			loffset.append(match.start())
		for right in content[2]:
			roffset.append(right.find('...') + len('...'))
		# Build the message from parts
		# Part 1: left up to first ellipsis
		msg = content[0][:loffset[0]]
		# Part 2: first right part without leading ellipsis
		msg = msg + content[2][0][roffset[0]:]
		# Part 3: newlines after first sentence up to second ellipsis
		msg = msg + content[0][loffset[0] + len(' ...'):loffset[1]]
		# Part 4: second right part without leading ellipsis.
		msg = msg + content[2][1][roffset[1]:]
	else:
		print("Warning: argc other than 1 or 2 encountered. Doing nothing.")
		break
	consequences[entry] = msg

pp = pprint.PrettyPrinter(indent = 4, width = 120)
pp.pprint(consequences)
