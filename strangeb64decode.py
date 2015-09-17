import base64
import re

def strangeb64decode(s):
    p=re.compile('\d| |\'|\(|\)|\[|\$|\^|\*|\-|\+|\?|\.|]|{|}|[a-z]|[A-Z]|`|!|~|@|#|%|&|_|=|;|:|"|,|/|<|>')
    result=[]
    if(len(s)%4==0):
        for i in xrange(0,len(s),4):
            segment=s[i:i+4]
            #print segment
            encrypts=[]
            encrypts.append(segment)
            for j in range(0,4):
                templist=[]
                for word in encrypts:
                    if word[j].isalpha():
                        templist.append(word[0:j]+word[j].lower()+word[j+1:4])
                        templist.append(word[0:j]+word[j].upper()+word[j+1:4])
                    else:
                        templist.append(word)
                encrypts=templist
            for word in encrypts:
                #print word
                m=base64.b64decode(word)
                for j in m:
                    if p.match(j)== None:
                        break
                    #pass
                else:
                    result.append(m)
                    break;#if break,only add the first one
        string=''
        for seg in result:
            string+=seg
    print 'result is :'+string
    return string

if __name__=='__main__':
    strangeb64decode('a2V5CWlzOnthd2Rpam9ub2lqb2lqZn0=')