import hashlib


def getMD5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()


def getSHA1(s):
    m = hashlib.sha1(s)
    return m.hexdigest()


def compute():
    str1 = 'TASC'
    str2 = 'O3RJMV'
    str3 = 'WDJKX'
    str4 = 'ZM'
    allstr = []
    for a in range(65, 91):
        for b in range(65, 91):
            for c in range(65, 91):
                temp = str1 + chr(a) + str2 + chr(b) + str3 + chr(c) + str4
                allstr.append(temp)
    print len(allstr)
    allmd5 = []
    for a in allstr:
        m = getMD5(a)
        if m[0] == 'e' and m[1] == '9' and m[2] == '0' and m[3] == '3' and m[7] == '4' and m[8] == 'd' and m[
            9] == 'a' and m[10] == 'b' and m[15] == '0' and m[16] == '8' and m[22] == '5' and m[23] == '1' and m[
            25] == '8' and m[26] == '0' and m[29] == '8' and m[30] == 'a':
            print a
            print m
            break


def breakSHA1():
    s = []
    for a in range(0, 10, 1):
        for b in range(0, 10, 1):
            for c in range(0, 10, 1):
                for d in range(0, 10, 1):
                    for e in range(0, 10, 1):
                        for f in range(0, 10, 1):
                            temp = str(a)+str(b) + str(c) + str(d) + str(e) + str(f)
                            print temp
                            sha = getSHA1(temp+'@DBApp')
                            if sha == '6E32D0943418C2C33385BC35A1470250DD8923A9'.lower():
                                print temp
                                return 0

def breakMD5():
    r=range(48,58,1)
    r+=range(65,91,1)
    r+=(range(97,123,1))
    #print r
    for a in r:
        for b in r:
            for c in r:
                for d in r:
                    for e in r:
                        for f in r:
                            temp = chr(a)+chr(b) + chr(c) + chr(d) + chr(e) + chr(f)+'123321'
                            print temp
                            sha = getMD5(temp)
                            if sha == '27019e688a4e62a649fd99cadaafdb4e'.lower():
                                print temp
                                return 0

breakMD5()