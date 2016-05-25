import random

def histogram(s):
	hist = {}
	for c in s:
		hist[c] = hist.get(c,0) + 1
		
	return hist
	
	
def print_letter(hist):
	l = 0.000
	for items in hist:
		l += hist[items]
	t = []
	for keys , value in hist.iteritems():
		t.append((value / l , keys))
		
		
	return t
	
	
if __name__ == '__main__':
	s = raw_input("hare:")
	hist = histogram(s)
	print print_letter(hist)
	
	