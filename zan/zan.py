from tkinter import *
class tuple:
	def __init__(self,parent,name):
		self.num=0
		self.frame=Frame(parent)
		self.frame.pack(side=TOP) #TOP must be UP Case
		self.name=Label(self.frame,text=name)
		self.name.config(font=("Times",20,"normal"))
		self.name.pack(side=LEFT)
		self.numLabel=Label(self.frame,text=str(self.num))
		self.numLabel.pack(side=LEFT)
		self.b=Button(self.frame,text="Good",command=(lambda:self.increase() or self.update()))
		self.b.pack(side=LEFT)
	def increase(self):
		self.num=self.num+1 #can not be num++
	def update(self):
		self.numLabel.config(text=self.num) #label must use config function to update on the fly
		#print(self.num)
root=Tk()
parent=Frame(root)
parent.pack()
f=open('zan.txt','rt')
for line in f:
	#print(line)
	tuple(parent,line.strip())
f.close()
root.title("点赞")
mainloop()