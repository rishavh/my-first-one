#this program   sort  a list of words
#on the basis of there length
#if length is same it select random one.
import random


def sort_word_list_by_random(word_list):
	""" word_list = list of strings.
	returns : sorted list of words.
	"""
	t = []
	for word in word_list:
		t.append((len(word),random.random(),word))
	t.sort(reverse = True)
	res = []
	for length, _ , word in t:
		res.append(word)
		
	return res
	
	
	
if __name__ == '__main__':
	n = int(raw_input("enter  the no of elimments you want in list :"))
	word_list = []
	for i in range(n):
		word_list.append(raw_input(">"))
		
		
	t = sort_word_list_by_random(word_list)
	
	
	for word in t:
		print word
		