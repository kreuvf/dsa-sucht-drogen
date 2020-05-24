# Create tables for inclusion in .tex files

# This script loops over all consequences files

import json
import re

# Populate files list
exec(compile(open("consequences.py", "r").read(), "consequences.py", 'exec'))
## The list named 'files' exists now!

# Prepare pairs of left-side text and right-side text
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

# Prepare single-string texts for consequences
conseqDict = {}

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
	# format() is required to convert {{}} to {}
	# {{}} were deliberately introduced for future flexbility (maybe ...)
	conseqDict[entry] = msg.format()

# Prepare consequences list in ascending order of 'severity'
conseqList = []

with open('./ranking.txt', 'r') as f:
	conseqOrder = list(f)

## Cut away trailing newlines
for index in range(len(conseqOrder[:-1])):
	conseqOrder[index] = conseqOrder[index][:-1]

## Build list
for conseq in conseqOrder:
	conseqList.append([conseqDict[conseq], conseq])

# Build strings with TeX Table rows
tablerows = []
## Starting severity is 2, the minimum value
severity = 2

## Determination of the last severity
## For 20 consequences and starting with severity 2, 19 other consequences come
## after it, making the max. severity 21
## -1 to correct off-by-one error
severityMax = severity + len(conseqList) - 1

for conseq in conseqList:
	conseqStr = conseq[0]
	if severity == severityMax:
		severityStr = str(severityMax) + '+'
	else:
		severityStr = str(severity)
	severityStr = severityStr + ' \\conseq{{{}}}'.format(conseq[1])
	tablerow = '{{{}}} & {{{}}} \\\\'.format(
		severityStr,
		conseqStr
	)
	tablerows.append(tablerow)
	severity = severity + 1

# Write output
with open('./consequences.tex', 'w') as f:
	for row in tablerows:
		print(row)
		f.write(row + '\n')
