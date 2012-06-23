import sys
import pickle    
import time    

def readFile ():
    
    flag = 0
    movies = []
    file = open('movies.list', 'r')
    
    for line in file :   
        if line.startswith('!') == True :
            flag = 1
        if flag == 1 and line.startswith('\n') == False : 
            movies.append(line)         
    file.close()
    return movies
    
def search (query, movies):
    
    flag = True
    
    for word in movies :
        if query in word :
            if flag == True :
                print '--- Keyword "%s" found ---' % query
                flag = False;
            print word
    
    if flag == True :
        print '--- Keyword "%s" DID NOT FOUND ---' % query
    
if __name__ == '__main__' :
        
    movies = readFile()
    print '****** File ready! ******'    
    
    while True :
        
        query = raw_input("Enter search query\n")
        if query == 'exit' :
            print ' *** Program Terminated ***'
            break
        start = time.time()
        
        for word in open(query, 'r') :
            keyword = word.split('\n')[0]
            search(keyword, movies)
            print '/*-------------------------------------------*/'     
            
        print '=============== Entire Searching End ==============='
        end = time.time()
        elapsed = end - start
        print '*************************'
        print '* time cost is %f *' % elapsed
        print '*************************'