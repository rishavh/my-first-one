from word_histogram import *

import random

from bisect import bisect

def random_word(hist):
	words_list = []
	freq_list = []
	q_sum = 0
	for keys, values in hist.iteritems():
		q_sum += values
		words_list.append(keys)
		freq_list.append(q_sum)
		
	z = random.randint(0,q_sum - 1)
	index = bisect(freq_list, z)
	return words_list[index]
	
	
if __name__ == '__main__':
	hist = make_histogram("king.txt")
	print random_word(hist)
	