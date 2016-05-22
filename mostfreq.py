# this program returns list of letters in incresing oder of frequency.
# takes a string



def make_histogram(s):
	"""
	takes  a string s
	returns a map to frequency from letters
	"""
	hist = {}
	for c in s:
		hist[c] = hist.get(c, 0) + 1
		
	return hist
	

	
def most_frequent_list(s):
	"""
	takes a string s
	returns a list of letters in incresing frequency
	"""
	hist = make_histogram(s)
	t = []
	for letters, freq in hist.iteritems():
		t.append((freq, letters))
	t.sort(reverse = True)
	res = []
	for freq, letters in t:
		res.append(letters)
		
	return res
	
	
def read_file(filename):
	"""
	returns the contants of file as string
	"""
	return open(filename).read()
	
	
	
	
if __name__ == '__main__':
	s = read_file(raw_input("enter the name of file hare :"))
	t = most_frequent_list(s)
	for x in t:
		print x
		
		
		
		
		