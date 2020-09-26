#!/usr/bin/python3

class Node():					#Node Class
	def __init__(self,data):		
		self.data  = data
		self.next = None

	def setData(self,data):		#These 4 functions are like setters and getters
		self.data = data

	def setNext(self,next):
		self.next = next

	def getData(self):
		return self.data
		
	def getNext(self):
		return self.next	




class LinkedList():
	def __init__(self,verbose=False,nodeCount=5):
		self.head = None
		self.verbose = verbose
		self.nodeCount = nodeCount
		self.MAX_NODES_SHOW = 20
	
	def addFirst(self,data):
		if self.head == None:
			newNode = Node(data)
			self.head = newNode

		else:
			newNode = Node(data)
			newNode.setNext(self.head)
			self.head = newNode

		if (self.verbose):
			print(f"[+] Added Node[{data}] In The Beginging")

	def addAfter(self,prevousNode,data):

		found,presentNode = self.is_found(self.head,prevousNode)
		if (found):
			if (presentNode.getNext() == None):
				self.add(data)
			else:
				newNode=Node(data)
				newNode.setNext(presentNode.next)
				presentNode.setNext(newNode)
			if (self.verbose):
				print(f"[+] Added Node[{data}] After Node[{prevousNode}]")
		else:
			print("[*] Sorry Node Not Found")


	def add(self,data):

		if self.head == None:
			newNode = Node(data)
			self.head = newNode
		else:
			newNode = Node(data)
			tempNode = self.head
			while (tempNode.getNext() != None):
				tempNode = tempNode.getNext()
			tempNode.setNext(newNode)
		if (self.verbose):
			print(f"[+] Added Node[{data}] In The End")

	def showNodes(self,data,limit,flag):
		top = ""
		middle = ""
		bottom = ""
		extension = ""
		for i in range(0,len(data)):

			length = len(str(data[i]))
			top += f"+{'='*(length+2)}+"
			middle += f"| {data[i]} |"
			bottom += f"+{'='*(length+2)}+"
			if (i!=limit-1 and i<len(data)-1):				#This function prints Nodes with diagram
				middle+="--->"
				top+= "    "
				bottom+= "    "
		if (flag):
			middle += "-|"
			bottom += " |"
			extension += " |"+"-"*(len(middle)-2)

		print(top)
		print(middle)
		print(bottom)
		print(extension)

	def console_data(self):

		data = []
		if (self.head == None):
			return "Empty List"

		tempNode = self.head
		if (tempNode.getNext() == None):
			data.append(tempNode.getData())		#This function will grab the data from nodes and forwards to  the above funtion

		while(tempNode):
			data.append(tempNode.getData())
			tempNode = tempNode.getNext()

		if (len(data) <= self.MAX_NODES_SHOW):
			count  = len(data)
			for i in range(0,len(data),self.nodeCount):
				flag = False
				count -=self.nodeCount
				if (count>0): flag = True 
				self.showNodes(data[i:i+self.nodeCount],self.nodeCount,flag)

		else:
			print(", ".join(map(str,data)))

	def is_found(self,node,data):				#This function checks if a particular nodes exists or not
		if (node == None):
			return False,None
		if (node.getData() == data):
			return True,node
		return self.is_found(node.getNext(),data)


	def deleteStart(self):
		if (self.head == None):
			print("[*] No Elements to remove")
		else:
			if (self.head.getNext() == None):
				del self.head
			else:
				tempNode = self.head
				self.head = tempNode.getNext()
				if (self.verbose):
					print(f"[-] Deleted Starting Node[{tempNode.getData()}] ")
				del tempNode

	def deleteEnd(self):

		if (self.head == None):
			print("No Elements to remove")
		if (self.head.getNext() == None):
			del self.head
		else:
			tempNode = self.head

			while (tempNode.getNext() != None):
				newTemp = tempNode
				tempNode = tempNode.getNext()

			newTemp.setNext(None)
			if (self.verbose):
				print(f"[-] Deleted End Node[{tempNode.getData()}] ")
			del tempNode


	def deleteNode(self,nodeData):
		if (self.is_found(self.head,nodeData)[0]):
			tempNode = self.head
			if (tempNode.getData()==nodeData):
				self.deleteStart()
			else:
				while (tempNode.getNext().getData() != nodeData):
					tempNode = tempNode.next
				if (tempNode.next == None):
					self.deleteEnd()
				targetNode = tempNode.next
				tempNode.next = targetNode.next
				del targetNode 
				if (self.verbose):
					print(f"[-] Deleted Node[{nodeData}] ")

		else:
			print("[*] No such Node Found")

def main():
	LL = LinkedList(verbose=True,nodeCount=5)
	LL.add(3)
	LL.add(4)
	LL.add(5)
	LL.addFirst(2)
	LL.addFirst(1)
	LL.addAfter(3,10)
	LL.console_data()
	LL.deleteEnd()
	LL.deleteStart()
	LL.console_data()
	LL.deleteNode(3)
	LL.console_data()


	

if __name__ == '__main__':
	main()
