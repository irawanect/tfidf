import math
def tf(n_terms, total_terms):
	tf = n_terms / total_terms
	return tf

def idf(n_doc, total_doc):
	idf = math.log10(n_doc / total_doc)
	return idf