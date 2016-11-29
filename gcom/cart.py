class Cart:
	def __init__(self):
		self.lst=[]
	def add(self, p_id):
		self.lst.append(p_id)
	def remove(self, p_id):
		self.lst.remove(p_id)
	def empty(self):
		if len(self.lst)==0:
			return True
		else:
			return False

c=""

def create():
	c1=Cart()
	global c
	c=c1

def remove():
	global c
	del c