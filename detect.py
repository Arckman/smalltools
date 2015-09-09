#-.-coding:utf-8 -.-
import urllib2,urllib
from threading import Thread
import re
import sched,time
from datetime import datetime
import pyodbc

scheduler=sched.scheduler(time.time,time.sleep)
dials={}
dials["FengRenjun"]="18852405661"
dials["XuDazhong"]="15062509771"
dials["Majun"]="13862376330"
dials["DingYoucheng"]="13773042941"
dials["WangJie"]="13862500500"
dials["FuHong"]="13962676398"
dials["LinFeng"]="13372175058"
dials["JingDongsheng"]="13372175060"
rkl=set([])
rklcl=set([])
today=""

def detect(method="queryZmRKL"):
	#method="queryZmRKL"
	#scheduler.enter(3600,0,detect,())
	global today
	url="http://10.134.91.114:8000/jsims4.0/zmMonitorQueryBatchAction.do?method="+method
	postdata={"start":"0","limit":"100","parentId":"0","areaId":"3"}
	#areId of suzhou:3
	#areId 10000 for all,used for test
	now=datetime.today()
	today=datetime.strftime(now,"%Y-%m-%d")
	postdata["beginTime"]=today
	postdata["endTime"]=today
	response=urllib2.urlopen(url,urllib.urlencode(postdata))
	resPage=response.read().decode("utf-8").encode("gbk")
	return resPage
	

def sendMsg(rows):
	#driver=IBM DB2 ODBC DRIVER
	global rkl,rklcl,dials
	strings="发现弱口令：\n".decode("utf-8").encode("gbk")
	newIssue=False
	temp=set([])
	for row in rows:
		ip=row["ipaddress"]
		temp.add(ip)
		if ip not in rkl:
			newIssue=True
			strings+=row["classname"]+":"+row["ipaddress"]+"\n"
	#stringTail="徐大中："+dials["XuDazhong"]+"|马骏："+dials["Majun"]+"|丁悠成："+dials["DingYoucheng"]+"|王劼："+dials["WangJie"]+"|傅洪："+dials["FuHong"]+"\n"
	#strings+=stringTail.decode("utf-8").encode("gbk")

	rklcl|=rkl-temp
	rkl|=temp
	if newIssue:
		print strings
		connectDB(strings,dials["FengRenjun"])
		#connecDB
	#print rkl
	#print rklcl
	

def connectDB(string,*people):
	dns="driver={IBM DB2 ODBC DRIVER};database=%s;hostname=%s;port=%s;protocol=tcpip;"%("DXPT","172.23.169.8","50000")
	conn=pyodbc.connect(dns+"uid=db2admin;pwd=DB2password")
	cursor=conn.cursor()
	for p in people:
		cmd="insert into DX_SEND(SJHM,DXNR) values ('%s','%s')"%(p,string)
		#print cmd
		cursor.execute(cmd)
	conn.commit()
	cursor.close()

def start():
	#print "start"
	global scheduler
	scheduler.enter(0,1,process,())
	print scheduler.queue

	#定时下午5点
	now=datetime.today()
	delay=60*60*17-now.minute*60-now.hour*3600
	if delay<0:
		delay=delay+24*3600
	#print delay
	scheduler.enter(delay,0,processDaily,())
	print scheduler.queue
	scheduler.run()
	
def process():
	global scheduler
	scheduler.enter(10*60,1,process,())
	print scheduler.queue
	resPage=detect()
	resPage=resPage.replace('true','True')
	#print resPage
	resData=eval(resPage)
	results=resData["results"]
	rows=resData["rows"]
	success=resData["success"]
	#print resData["rows"][0]["classname"]
	#rows=[rows[0]]
	if success==True and results>0:
		sendMsg(rows)

def processDaily():
	global today,rkl,rklcl,scheduler
	scheduler.enter(24*3600,0,processDaily,())
	print scheduler.queue
	rklN=len(rkl)
	rklclN=len(rklcl)
	rklsyN=rklN-rklclN
	string=today+utf2gbk("弱口令情况：\n")
	string+=utf2gbk("共发现%s条，处理%s条，未处理%s条。\n"%(rklN,rklclN,rklsyN))
	if rklsyN!=0:
		string+=utf2gbk("未处理ip：\n")
		temp=rkl-rklcl
		for r in temp:
			string+=r+"\n"
	print string
	connectDB(string,dials["FengRenjun"],dials["JingDongsheng"])
	rkl=set([])
	rklcl=set([])

def utf2gbk(string):
	return string.decode("utf-8").encode("gbk")

#__main
t=Thread(target=start,name="detect")
#t.setDaemon(True)
t.start()

