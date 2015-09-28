#uucode, an encryptyion
#uuencode:a word consisted of 6 bits instead of 8
import bitarray

def uuencode(s):
    #s=str(s)
    res=''
    bitsa=bitarray.bitarray()
    bitsa.fromstring(s)
    if len(bitsa)%6==0:
        bits=int(bitsa.to01(),2)
        op=0b111111
        for i in xrange(0,len(bitsa)/6):
            #print bits&op
            res=chr(bits&op+0x20)+res
            bits>>=6
        print "encoding result is: "+res
    else:
        print "Not a valid string for encoding!"
    return res

def uudecode(s):
    res=''
    if len(s)%4==0:
        bytea=bytearray(s)
        print bytea
        bs=''
        for byte in bytea:
            b='{:0=6b}'.format(byte-0x20)
            print b
            bs+=b
        bs=bitarray.bitarray(bs)
        res=bs.tostring()
        print "decoding result is: "+res
    else:
        print "Not a valid string for decoding!"
    return res

if __name__=='__main__':
    #uuencode('asd')
    uudecode(r')^KN')
    #uudecode(r'MR,O)^KNYU>;*Q[*[P_?#Q+"AHZS6Q\G,LKNYNZ.LR;;2LK*[N^&CK+/VN/;,MXK:\TJJ]RKZAQ-36K:&CH:,*M/.XQ;3PL+B^S<K\'U>+1^;#)=V-T9GMU=75U*=65N8V]D95]??0``')