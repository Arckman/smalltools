f=open('D:\\1.txt','r')
inp=f.readlines()
path=[[None for col in range(27)]for row in range(27)]
for line in inp:
    ss=line.split(' ')
    #print ss
    if len(ss)>=2:
        path[int(ss[0])][int(ss[1])]=int(ss[2])
#print path
def walk(source,total,route):
    if source==26:
        print route+":"+str(total)
        return
    else:
        outgo=path[source]
        passed=route.split(',')
        for i in range(27):
            if str(i) not in passed and outgo[i]!=None:
                walk(i,total+outgo[i],route+','+str(i))


walk(1,0,'1')


