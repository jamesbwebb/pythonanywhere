# This might work better if I don't try to output the data to the same file...
import csv

f = open('H3.csv', 'r')
nf = open('H4.csv', 'w')
for line in f.readlines():
	l = line.split(',')
	answer = l[2]
	newline = answer[16:].strip() + l[1].strip()
	writer = csv.writer(nf, delimiter = ',')
	writer.writerow(newline)
	f.close()
	nf.close()

# This worked but added an extra , in between the characters in variable newline[0]
