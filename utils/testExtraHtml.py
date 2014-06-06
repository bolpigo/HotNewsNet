from sgmllib import SGMLParser  
class GetIdList(SGMLParser):  
	def reset(self):  
        	self.IDlist = []  
        	self.flag = False  
        	self.getdata = False  
        	self.verbatim = 0  
        	SGMLParser.reset(self)  
          
    	def start_div(self, attrs):  
        	if self.flag == True:  
        		self.verbatim +=1   
        		return  
        	for k,v in attrs: 
        		if k == 'class' and v == 'entry-content':  
                		self.flag = True  
                		return  
  
    	def end_div(self):  
        	if self.verbatim == 0:  
            		self.flag = False  
        	if self.flag == True:  
            		self.verbatim -=1  
	def start_p(self, attrs):  
        	if self.flag == False:  
            		return  
        	self.getdata = True  
          
    	def end_p(self):  
        	if self.getdata:  
            		self.getdata = False  
  
    	def handle_data(self, text):  
        	if self.getdata:  
            		self.IDlist.append(text)  
              
    	def printID(self):  
        	for i in self.IDlist:  
            		print i  
the_page ='''''<html> 
<head> 
<title>test</title> 
</head> 
<body> 
<h1>title</h1> 
<div class='entry-content'> 
<div class= 'ooxx'>---------1</div> 
<p>++++++++1</p> 
<p>++++++++2</p> 
...
<p>++++++++n</p> 
<div class= 'ooxx'>------------2<div class= 'ooxx'>----------3</div></div> 
</div> 
<div class='content'> 
<p>+-+-+-+-1</p> 
<p>+-+-+-+-2</p> 
...
<p>+-+-+-+-n</p> 
</div> 
</body> 
</html> 
'''  
lister = GetIdList()  
lister.feed(the_page)  
lister.printID()  
