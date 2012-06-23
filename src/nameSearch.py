import sys
import pickle
import time

def readPickle (alphabet):
	
 	dic = {}
 	extension = '.p'
 	for i in range(len(alphabet)) :
 		index = alphabet[i]
 		searchfile = index + extension
 	 	pkl_file = open(searchfile, 'rb')
	 	data = pickle.load(pkl_file)
	 	dic[index] = data
 		print searchfile
 	return dic

	
def search (keyword, index1, index2, dic):
	
	hasResult = True		
	
	if index2 == None :
		if keyword in dic[index1] :
			hasResult = False
#			print 'Actor or Actress name is %s' % keyword
			print '***********************************************'
			print 'Movie List For Actor or Actress "%s"' % keyword
			print '***********************************************'
			for i in dic[index1][keyword] :
				print i
	else :
		
		if index2 in dic[index1] :
			if keyword in dic[index1][index2] :
				hasResult = False
#				print 'Actor or Actress name is %s' 
				print '***********************************************'
				print 'Movie List For Actor or Actress "%s"' % keyword
				print '***********************************************'
				for i in dic[index1][index2][keyword] :
					print i
		
	if hasResult == True :
		print '"%s" is not existed in the Database' % keyword	
		
#	print '*************************************************'
	
def searchPattern(query):	
	
	queryword = open(query, 'r')
	for word in queryword :
		keyword = word.split('\n')[0]
		newword = [x.upper() for x in keyword.split(',')]
		index1 = newword[0][0]
		if len(keyword.split(',')) == 2 :
			if len(newword[1]) != 0 :
				index2 = newword[1][1:][0]
			else :
				index2 = None
		else :
			index2 = None
			
		search (keyword, index1, index2, dic)
		print '/*-------------------------------------------*/' 
		
if __name__ == '__main__' :
	
	query = ''
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	
	dic = readPickle(alphabet)
	
	while True :
		print '****** Start ******'
		query = raw_input("Enter a query file\n")
		if query == 'exit' :
			print '****** Program Terminated *******'
			break
		searchPattern(query)
		print '=============== Search End ==============='