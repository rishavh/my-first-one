




def signature(s):
	"""
	takes a string s
	returns a oder string
	"""
	z = list(s)
	z.sort()
	t = ''.join(z)
	return t
	
	
	
	
def annagrams_set(filename):
	"""
	returns a map of annagrams_set
	"""
	h = {}
	fin = open(filename)
	for line in fin:
		word = line.strip().lower()
		t = signature(word)
			
		if t not in h:
			h[t]= [word]
		else:
			h[t].append(word)
			
	return h
	
	
	
def print_annagram(d):
	"""
	print the annagrams_set:
	d is  a dict
	"""
	for v in d.values():
		if len(v) > 1:
			print v

def print_annagram_in_oder(d):
	"""
	print annagrams_set in incresing oder of items
	"""
	t = []
	for v in d.values():
		if len(v) > 1:
			t.append((len(v), v))
	t.sort()
	
	for length, values in t:
		print values
		
		
		
		
		
		
if __name__ == '__main__':
	h = annagrams_set(raw_input("enter the name of file hare :"))
	
	
	print_annagram(h)
	print_annagram_in_oder(h)
	
