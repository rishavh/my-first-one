import random

from probebilty import *


def histogram(s):
	hist = {}
	for  c in s:
		hist[c] = hist.get(c,0) + 1
		
		
	return hist
	
	
	
	
def choes_random(hist):
	t = []
	for items in hist:
		for i in range(hist[items]):
			t.append(items)
			
			
	return random.choice(t)
	
	
def stats(hist):
	t = {}
	for items in hist:
		for i in range(1000):
			if choes_random(hist) == items:
				t[items] = t.get(items, 0) + 1
	z = []
	for keys, value in t.iteritems():
		z.append((keys, value / 1000.00))
		
	return z
	
	

	
	

if __name__ == '__main__':
		s = raw_input(" enter the string hare :")
		hist = histogram(s)
		
		print print_letter(hist)
		print choes_random(hist)
		print stats(hist)
		
		
		
	
	
