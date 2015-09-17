
class coder:
	charbase="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	@staticmethod
	def encode(offset):
		if len(coder.charbase)!=0x40:
			coder.charbase="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
		if offset>=0 and offset<=0x40:
			return coder.charbase[offset]
		else:
			return -1

	@staticmethod
	def decode(c):
		if len(coder.charbase)!=0x40:
			coder.charbase="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
		if len(c)!=1:
			return -1
		return coder.charbase.find(c)
