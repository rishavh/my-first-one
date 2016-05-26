import string


def make_histogram(filename):
	hist = {}
	fin = open(filename)
	for line in fin:
		process_line(line, hist)
		
	return hist
	
	
def process_line(line, hist):
	line = line.replace('-', '')
	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		hist[word] = hist.get(word,0) + 1
		
		
def different_word(hist):
	return len(hist)
	
def most_commen_word(hist):
	t = []
	for keys ,values in hist.iteritems():
		t.append((values, keys))
		
	t.sort(reverse = True)
	return t
if __name__ == '__main__':
			hist = make_histogram ('king.txt')
			print different_word(hist)
			num = int(raw_input("enter the number of word you want to p which are common :"))
			
			
			t = most_commen_word(hist)
			
			for x, y in t[0:num]:
				print y,x
				
			
	
		