import time
import random

def make_dictionarie():
	fin = open (t)
	d = {}
	for line in fin:
		word = line.strip()
		d[word] = random.randint(1, 10)
		
	return d



def is_present(d, word):
	if word in d:
		return True
		
if __name__ == '__main__':
	t = raw_input("enter the name of file :")
	word = raw_input("enter the word :")
	time_start = time.time()
	my_dict = make_dictionarie()
	print " the  word you search is present:",is_present(my_dict, word)
	total_time = time.time() - time_start
	print "your's had taken %s seconds"%total_time
	
	
	