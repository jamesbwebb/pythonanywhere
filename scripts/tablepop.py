from learnkana.models import KanaCheck

with open('hiragana.csv', 'r') as file:
	for line in file.readlines():
		ls = line.split(',')
		x = ls[0]
		y = ls[1]
		t = KanaCheck(text=x, hir=y)
		t.save()
		print('saved'

#t = KanaCheck(text=x , hir=y)
