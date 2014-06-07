from sgmllib import SGMLParser  
class GetIdList(SGMLParser):  
	def reset(self):  
        	self.IDlist = []  
        	self.flag = False  
        	self.getdata = False  
        	self.verbatim = 0  
        	SGMLParser.reset(self)  
	def start_p(self, attrs):  
        	self.getdata = True  
          
    	def end_p(self):  
        	if self.getdata:  
            		self.getdata = False  
		if self.flag:
			self.flag = False
  
    	def handle_data(self, text):  
        	if self.getdata:  
            		self.IDlist.append(text)  
              
    	def printID(self):  
        	for i in self.IDlist:  
            		print i  
