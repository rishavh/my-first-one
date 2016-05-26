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



if __name__ == '__main__':
			hist = make_histogram ('king.txt')
			print hist
			
	
		