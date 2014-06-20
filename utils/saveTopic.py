import re
import MySQLdb
import urllib2
import datetime
import sys
import chardet
from extrahtmlppp import GetIdList
def saveBaiduTopics():
	input1 = open('./source/baidu.txt','r')
	try:
		content1 = input1.read()
	finally:
		input1.close()
	
	wordb = "\"index\":"
	worde = "imgList.push" 
	index1 = [m.start() for m in re.finditer(wordb,content1)]
	index2 = [m.start() for m in re.finditer(worde,content1)]
	output1 = open('.\\source\\topic.txt','w+')
	for i in range(0,len(index1)):
		content=content1[index1[i]:index2[i]]
		wordt = "\"abs\":"
		index3 = [m.start() for m in re.finditer(wordt,content)]
		content=content[:index3[0]]
		if i == 0:
			output1.write("                ")
		output1.write(content)
	output1.close()
	input = open('.\\source\\topic.txt','r')
	content = input.read()
	input.close()
	titleword = "\"title\":"
	urlword = "\"url\":"
	imgurlword = "\"imgUrl\":"
	titleindex=[m.start() for m in re.finditer(titleword,content)]
	urlindex=[m.start() for m in re.finditer(urlword,content)]
	imgurlindex=[m.start() for m in re.finditer(imgurlword,content)]
	output = open('.\\source\\test.txt','w')
	try:
		conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='126373',db='hotnews',port=3306)
		cur=conn.cursor()
		cur.execute('delete from index_newsinfo')
		cur.execute('set names gbk')
		val=[]
		for i in range(0,len(titleindex)):
			title = content[titleindex[i]+len(titleword)+1:urlindex[i]-2]
			url = content[urlindex[i]+len(urlword)+1:imgurlindex[i]-2]
			t = len(content)-2
			if i < len(titleindex)-1:
				t=titleindex[i+1]-2
			imgurl = content[imgurlindex[i]+len(imgurlword)+1:t]
			splitword="\""
			ii=[m.start() for m in re.finditer(splitword,title)]
			title=title[ii[0]+1:ii[1]]
			ii=[m.start() for m in re.finditer(splitword,url)]
			url=url[ii[0]+1:ii[1]]
			url = url.replace("\\","")
			ii=[m.start() for m in re.finditer(splitword,imgurl)]
			imgurl=imgurl[ii[0]+1:ii[1]]
			imgurl = imgurl.replace("\\","")
			#print imgurl
			output.write("\n")
			output.write(title)
			output.write("\n")
			output.write(url)
			output.write("\n")
			output.write(imgurl)
			imgname = str(i)+'.jpg'
			outimg=open("../index/static/baidu/images\\"+imgname,'wb')
			data=urllib2.urlopen(imgurl).read()
			outimg.write(data)
			outimg.close()
			data=urllib2.urlopen(url).read()
			typeEncode = sys.getfilesystemencoding()
			infoencode = chardet.detect(data).get('encoding','utf-8')
			data = data.decode(infoencode,'ignore').encode(typeEncode)
			lister = GetIdList()
			lister.feed(data)
			#lister.printID()
			listdd=lister.IDlist
			data=""
			data=data.join(listdd)
			data = data.replace(" ","")
			#print data
			datett = datetime.datetime.now()
			val.append((0, 1, url, title, imgurl, imgname, data, datett))
		cur.executemany('insert into index_newsinfo(source, format, url, title, imgurl, imgname, content, touchTime) values(%s,%s,%s,%s,%s,%s,%s, %s)',val)
		conn.commit()
		cur.close()
		conn.close()
		output.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
def saveTencentTopics():
	input1 = open('./source/tencent.txt','r')
	try:
		content1 = input1.read()
	finally:
		input1.close()
	
	wordb = "<div class=\"bd\" style=\"margin-bottom:10px;\">"
	worde = "<div class=\"pageInfo\">" 
	index1 = [m.start() for m in re.finditer(wordb,content1)]
	index2 = [m.start() for m in re.finditer(worde,content1)]
	content = content1[index1[0]+len(wordb):index2[0]]
	word1="<a href=\""
	word2="bosszone=\""
	word3="<img src=\""
	word4="alt=\""
	word5="<p>"
	index1 = [m.start() for m in re.finditer(word1,content)]
	index2 = [m.start() for m in re.finditer(word2,content)]
	index3 = [m.start() for m in re.finditer(word3,content)]
	index4 = [m.start() for m in re.finditer(word4,content)]
	index5 = [m.start() for m in re.finditer(word5,content)]
	try:
		conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='126373',db='hotnews',port=3306)
		cur=conn.cursor()
		cur.execute('set names gbk')
		val=[]
		for i in range(0,len(index1)):
			url = content[index1[i]+len(word1):index2[i]-2]
			imgurl = content[index3[i]+len(word3):index4[i]-2]
			title = content[index4[i]+len(word4):index5[i]-3]
			#print imgurl
			imgname = str(i)+'.jpg'
			outimg=open("../index/static/tencent/images\\"+imgname,'wb')
			data=urllib2.urlopen(imgurl).read()
			outimg.write(data)
			outimg.close()
			data=urllib2.urlopen(url).read()
			typeEncode = sys.getfilesystemencoding()
			infoencode = chardet.detect(data).get('encoding','utf-8')
			data = data.decode(infoencode,'ignore').encode(typeEncode)
			lister = GetIdList()
			lister.feed(data)
			#lister.printID()
			listdd=lister.IDlist
			data=""
			data=data.join(listdd)
			data = data.replace(" ","")
			#print data
			datett = datetime.datetime.now()
			val.append((1, 1, url, title, imgurl, imgname, data, datett))
		cur.executemany('insert into index_newsinfo(source, format, url, title, imgurl, imgname, content, touchTime) values(%s,%s,%s,%s,%s,%s,%s, %s)',val)
		conn.commit()
		cur.close()
		conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
def saveSohuTopics():
	input1 = open('./source/sohu.txt','r')
	try:
		content1 = input1.read()
	finally:
		input1.close()
	
	wordb = "<ul class=\"picLeft\""
	worde = "<div class=\"btn blue\"" 
	index1 = [m.start() for m in re.finditer(wordb,content1)]
	index2 = [m.start() for m in re.finditer(worde,content1)]
	content = content1[index1[0]+len(wordb):index2[0]]
	word1="<a href=\""
	word2="src=\""
	word3="width="
	word4="target=\"_blank\""
	word5="</a></em>"
	index1 = [m.start() for m in re.finditer(word1,content)]
	index2 = [m.start() for m in re.finditer(word2,content)]
	index3 = [m.start() for m in re.finditer(word3,content)]
	index4 = [m.start() for m in re.finditer(word4,content)]
	index5 = [m.start() for m in re.finditer(word5,content)]
	try:
		conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='126373',db='hotnews',port=3306)
		cur=conn.cursor()
		cur.execute('set names gbk')
		val=[]
		for i in range(0,len(index2)):
			url = content[index1[i*2]+len(word1):index4[i*2]-2]
			imgurl = content[index2[i]+len(word2):index3[i]-2]
			url = url.replace("\"","")
			imgurl = imgurl.replace("\"","")
			title = content[index4[i*2+1]+len(word4)+1:index5[i]]
			#print imgurl
			imgname = str(i)+'.jpg'
			outimg=open("../index/static/sohu/images\\"+imgname,'wb')
			data=urllib2.urlopen(imgurl).read()
			outimg.write(data)
			outimg.close()
			data=urllib2.urlopen(url).read()
			typeEncode = sys.getfilesystemencoding()
			infoencode = chardet.detect(data).get('encoding','utf-8')
			data = data.decode(infoencode,'ignore').encode(typeEncode)
			#lister = GetIdList()
			#lister.feed(data)
			#lister.printID()
			#listdd=lister.IDlist
			#data=""
			#data=data.join(listdd)
			#data = data.replace(" ","")
			#print data
			datett = datetime.datetime.now()
			val.append((2, 1, url, title, imgurl, imgname, data, datett))
		cur.executemany('insert into index_newsinfo(source, format, url, title, imgurl, imgname, content, touchTime) values(%s,%s,%s,%s,%s,%s,%s, %s)',val)
		conn.commit()
		cur.close()
		conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
def saveNeteasyTopics():
	input1 = open('./source/neteasy.txt','r')
	try:
		content1 = input1.read()
	finally:
		input1.close()
	
	wordb = "<ul class=\"widget-slide-contents-piclist\">"
	worde = "<div class=\"widget-slide-ctrl widget-slide-1-ctrl\">" 
	index1 = [m.start() for m in re.finditer(wordb,content1)]
	index2 = [m.start() for m in re.finditer(worde,content1)]
	content = content1[index1[0]+len(wordb):index2[0]]
	word1="<a class = \"left\"  href=\""
	word2="><img width="
	word3="alt=\""
	word4="title=\""
	word5="src=\""
	word6="></a>"
	index1 = [m.start() for m in re.finditer(word1,content)]
	index2 = [m.start() for m in re.finditer(word2,content)]
	index3 = [m.start() for m in re.finditer(word3,content)]
	index4 = [m.start() for m in re.finditer(word4,content)]
	index5 = [m.start() for m in re.finditer(word5,content)]
	index6 = [m.start() for m in re.finditer(word6,content)]
	try:
		conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='126373',db='hotnews',port=3306)
		cur=conn.cursor()
		cur.execute('set names gbk')
		val=[]
		for i in range(0,len(index2)):
			url = content[index1[i]+len(word1):index2[i]-1]
			imgurl = content[index5[i]+len(word5):index6[i]-1]
			url = url.replace("\"","")
			imgurl = imgurl.replace("\"","")
			title = content[index4[i]+len(word4):index5[i]-2]
			#print imgurl
			imgname = str(i)+'.jpg'
			outimg=open("../index/static/neteasy/images\\"+imgname,'wb')
			data=urllib2.urlopen(imgurl).read()
			outimg.write(data)
			outimg.close()
			data=urllib2.urlopen(url).read()
			typeEncode = sys.getfilesystemencoding()
			infoencode = chardet.detect(data).get('encoding','utf-8')
			data = data.decode(infoencode,'ignore').encode(typeEncode)
			#lister = GetIdList()
			#lister.feed(data)
			#lister.printID()
			#listdd=lister.IDlist
			#data=""
			#data=data.join(listdd)
			#data = data.replace(" ","")
			#print data
			datett = datetime.datetime.now()
			val.append((3, 1, url, title, imgurl, imgname, data, datett))
		cur.executemany('insert into index_newsinfo(source, format, url, title, imgurl, imgname, content, touchTime) values(%s,%s,%s,%s,%s,%s,%s, %s)',val)
		conn.commit()
		cur.close()
		conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
