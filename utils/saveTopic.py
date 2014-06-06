import re
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
for i in range(0,len(index1)-1):
	content=content1[index1[i]:index2[i]]
	wordt = "\"abs\":"
	index3 = [m.start() for m in re.finditer(wordt,content)]
	content=content[:index3[0]]
	if i == 0:
		output1.write("                ")
	output1.write(content)
output1.close()
