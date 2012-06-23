import sys
import pickle

class BuildIndex :
    
    def __init__(self, f) :
   
        self.f = f 
        self.dic = {}
        self.key = ''
        self.header = ''
        self.templist = []
        self.previousHeader = 'A'
        
    def main (self):    
        
        flag = 0
        self.header = ''
        
        for line in self.f :
            
            if flag == 3 :
                break
            
            if line.startswith('\n') == False :
            
                if flag == 0 :
                    if line.startswith(self.previousHeader) == True :
                        # start to build
                        flag = 1

                
                if flag == 2 :
    #                print line
                    if line.startswith('\t') == False :
                        tag = self.filter(line)   
                        if tag is False :
                            flag = 1
                            currentHeader = self.getCurrentHeader(line)
                            if self.previousHeader != currentHeader :
                                self.rewriteFile()
                                self.previousHeader = currentHeader

                if flag == 1 :
    #                print line
                    tag = self.filter(line)
                    if tag is True :
                        flag = 2
                 
                if flag == 1 :
                    self.build(line) 
                        
                # reach the end
                if self.previousHeader == 'Z' and line.startswith('\t') == False:
                    currentHeader = self.getCurrentHeader(line)
                    if currentHeader != self.previousHeader :
                        self.rewriteFile()
                        flag = 3
                         
              
    def build (self, line):
                
        index = 0 
        # same header and same name         
        if line.startswith('\t') == True :
            self.recordWithoutKey(line)
        
        elif line.startswith('\t') == False and line.startswith('\n') == False :
            
            currentHeader = self.getCurrentHeader(line)
            # switch header 
            if currentHeader != self.previousHeader :  
                self.rewriteFile()
                newline = line.split('\t')[0].split(',')
                if len(newline) == 2 :
                    newline = [x.upper() for x in newline[1]]
                    if len(newline) != 0 :
                        self.header = newline[1]
                    else :
                        self.header = None
                else :
                    self.header = None
                
                self.key = line.split('\t')[0]
#                print self.key
#                print self.header 
                self.recordWithKey(line)
                self.previousHeader = currentHeader               
                    
            # same header but switch name
            elif currentHeader == self.previousHeader :    
                newline = line.split('\t')[0].split(',')  
                if len(newline) == 2 :
                    
                    newline = [x.upper() for x in newline[1]]
                    if len(newline) != 0 :
                        self.header = newline[1]
                    else :
                        self.header = None

                else :
                    self.header = None
                
                  
                self.key = line.split('\t')[0]  
#                print self.key
#                print self.header 
                self.templist = [] 
                self.recordWithKey(line)
                
    def getCurrentHeader (self, line):
        ls = [x.upper() for x in line.split('\t')[0]]
        return ls[0]
    
    def rewriteFile (self):
        extension = '.p'
        filename = self.previousHeader + extension
        actorData = pickle.load(open(filename, 'rb'))
        
        for i in self.dic :
            newdic = {}
            if i in actorData :
                for j in actorData[i] :
                    if i != 'Soller':
                        newdic[j] = actorData[i][j]    
                for j in self.dic[i] :
                    if i != 'Soller' :
                        newdic[j] = self.dic[i][j]
                        
                if i != 'Soller':        
                    actorData[i] = newdic
                else :
                    actorData[i] = self.dic[i]
                
            else :
                actorData[i] = self.dic[i]
            
        pickle.dump(actorData, open(filename, 'wb'))
        print filename
        self.dic.clear()
        self.templist = []
        
    def recordWithKey (self, line):
        
        for j in line.split('\t')[1:] :
            if j != "" :
                self.templist.append(j)
        if self.header == None :
            self.dic[self.key] = self.templist   
        else :

            if self.header not in self.dic :
                self.dic[self.header] = {} 
            self.dic[self.header][self.key] = self.templist 
                        
    def recordWithoutKey (self, line):
        for j in line.split('\t') :
            if j != "" :
                self.templist.append(j)
     
    def filter (self, line):      
        result = False
        pattern = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                   'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                   ',','-','.',' ',"'"]
        
        for i in line.split('\t')[0] :
            if i not in pattern :
                result =  True
#        print result
        
        return result
        
if __name__ == '__main__' : 
    
    flag = 0;
    f = open('actresses.list','r')
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AAA']
    builder = BuildIndex(f)
    builder.main()
        
            
        
    
    