from annagramset import *

def metathesis_pare(d):
	"""
	d: dict
	print all metathesis_pare
	"""
	for annagram in d.itervalues():
		for word1 in annagram:
			for word2 in annagram:
				if word1 < word2 and word_distance(word1,word2) == 2:
					print word1,word2
					
					
					
def word_distance(word1,word2):
	"""
	calculate the distance between two words.
	"""
	assert len(word1) == len(word2)
	
	count = 0
	for c1,c2 in zip(word1,word2):
		if c1 != c2:
			count += 1
	return count
	
	
	
	
			
			
			
				
if __name__ == '__main__':
	h = annagrams_set(raw_input("enter the name of file hare:"))
	metathesis_pare(h)
	
	
	