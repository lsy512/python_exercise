import numpy as np
import pickle 
i=1
running=1

def a(x=1,y=2):
	'''asdasdasdasd
	asdasdasdasd
	asdasdasdasd'''
	print x*y



print dir(pickle)


while running:
	a(3,3)
	print a.__doc__
	j=int(raw_input("input a int:"))
	for k in range(0,j):
		print k

	if i==j:
		print '='
	elif i>j:
		print '>'
	else:
		print '<'
		running=0
