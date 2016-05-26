from word_histogram import *


def different_word(d1, d2):
	h = {}
	for keys in d1:
		if keys not in d2:
			h[keys] = None
			
	return h
	
	
	
	
if __name__ == '__main__':
	d1 = make_histogram("king.txt")
	d2 = make_histogram("words.txt")
	result = different_word(d1, d2)
	for keys in result:
		print keys
		
	
	