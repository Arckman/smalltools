#-.-coding:utf-8-.-
import re
import xlwt
import sys
#sys.setdefaultencoding("utf-8")
f=open("index.html","rt")
data=f.read()
string=data.decode("utf-8-sig").encode("gbk")
matchesVD=re.findall("<tr class=\"even vh\".*?</table>",string,re.M|re.S)
matchesD=re.findall("<tr class=\"odd vm\".*?</table>",string,re.M|re.S)
print len(matchesVD)
print len(matchesD)
#print "受影响主机"
#str1="受影响主机".decode("utf-8")
nameP=re.compile("<a.*?</a>",re.M|re.S)
s="<td.*?width=\"20%\">受影响主机</td>.*?</td>"
s=s.decode("utf-8").encode("gbk")
ipP=re.compile(s,re.M|re.S)
s="<td  valign=\"top\"  width=\"20%\">详细描述</td>.*?</td>"
s=s.decode("utf-8").encode("gbk")
msgP=re.compile(s,re.M|re.S)
s="<td  valign=\"top\">解决办法</td>.*?</td>"
s=s.decode("utf-8").encode("gbk")
solveP=re.compile(s,re.M|re.S)

#print matchesVD[0]
#print "match result:"
#print solveP.search(matchesVD[0]).group()

workbook=xlwt.Workbook()
sheet=workbook.add_sheet("sheet1")
for i in range(0,len(matchesVD)):
#for i in range(0,1):
	#name
	s=nameP.search(matchesVD[i]).group()
	s=s.replace("</a>","")
	s=s.split(">")[1]
	sheet.write(i,0,s.decode("gbk"))
	#ip
	s=ipP.search(matchesVD[i]).group()
	ips=re.findall("<a href=\".*?</a>",s,re.M|re.S)
	s=""
	for ip in ips:
		ipstr=ip.replace("</a>","").split(">")[1]
		s+=ipstr
		s+="\n\t"
		#print s
	sheet.write(i,1,s.decode("gbk"))
	#详情
	s=msgP.search(matchesVD[i]).group()
	s=s.split("</td>")[1].replace("<br />"," ").split(">")[1]
	#print s
	sheet.write(i,2,s.decode("gbk"))
	s=solveP.search(matchesVD[i]).group()
	s=s.replace("<br />","").split("</td>")[1].split(">")[1]
	#print s
	sheet.write(i,3,s.decode("gbk"))
for i in range(0,len(matchesD)):
#for i in range(0,1):
	#name
	s=nameP.search(matchesD[i]).group()
	s=s.replace("</a>","")
	s=s.split(">")[1]
	sheet.write(i+len(matchesVD),0,s.decode("gbk"))
	#ip
	s=ipP.search(matchesD[i]).group()
	ips=re.findall("<a href=\".*?</a>",s,re.M|re.S)
	s=""
	for ip in ips:
		ipstr=ip.replace("</a>","").split(">")[1]
		s+=ipstr
		s+="\n\t"
		#print s
	sheet.write(i+len(matchesVD),1,s.decode("gbk"))
	#详情
	s=msgP.search(matchesD[i]).group()
	s=s.split("</td>")[1].replace("<br />"," ").split(">")[1]
	#print s
	sheet.write(i+len(matchesVD),2,s.decode("gbk"))
	s=solveP.search(matchesD[i]).group()
	s=s.replace("<br />","").split("</td>")[1].split(">")[1]
	#print s
	sheet.write(i+len(matchesVD),3,s.decode("gbk"))
workbook.save("test.xls")