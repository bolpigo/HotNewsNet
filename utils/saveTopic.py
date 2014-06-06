import re
import MySQLdb
import urllib
input1 = open('./source/baidu.txt','r')
try:
	content1 = input1.read()
finally:
	input1.close()

wordb = "\"index\":"
worde = "imgList.push" 
index1 = [m.start() for m in re.finditer(wordb,content1)]
index2 = [m.start() for m in re.finditer(worde,content1)]
output1 = open('.\\source\\topic.txt','w')
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
out = open('.\\source\\test.txt','w')
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
		ii=[m.start() for m in re.finditer(splitword,imgurl)]
		imgurl=imgurl[ii[0]+1:ii[1]]
		out.write("\n")
		out.write(title)
		out.write("\n")
		out.write(url)
		out.write("\n")
		out.write(imgurl);
		outimg=open(".\\images\\"+str(i)+'.jpg','wb')
		data=urllib.urlopen(imgurl).read()
		outimg.write(data)
		outimg.close()
		val.append((0, 1, url, title, imgurl))
	cur.executemany('insert into index_newsinfo(source,format,url,title,imgurl) values(%s,%s,%s,%s,%s)',val)
	conn.commit()
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
out.close()
