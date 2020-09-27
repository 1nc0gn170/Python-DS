#!/usr/bin/python3 

class Stack():
	def __init__(self,size=15,verbose=False):
		self.stack = []
		self.MAX_STACK = size
		self.MAX_STACK_PRINT = 15
		self.verbose = verbose


	def stackMax(self):
		return max(self.stack)

	def printStack(self):
		if (self.stackLen()>self.MAX_STACK_PRINT):
			print(", ".join(self.stack))
		else:
			if (self.stackLen()>0):
				MAX = len(str(self.stackMax()))
				print()
				for index,item in enumerate(self.stack[::-1]):
					print("|  "+str(item).rjust(MAX," ")+"  |")
					print("+"+"-"*(MAX+4)+"+")
				print()
			else:
				print("[-] No Elements Found")



	def stackLen(self):
		return len(self.stack)

	def push(self,data):
		if (self.stackLen() >= self.MAX_STACK):
			print(f"[+] Stack Overflow. Reached Maximum ")
			return
		self.stack.append(data)
		if (self.verbose):
			print(f"[+] Pushing {data} on to the stack")
		return


	def pop(self):
		if (self.stackLen() <= 0):
			print("[-] Stack Underflow. Reached Minimum")
			return
		pop = self.stack.pop()
		if (self.verbose):
			print(f"[-] Poping  {pop} out of the stack")
		return

	def peek(self):
		if (self.stackLen() == 0):
			return None
		else:
			peek = self.stack[-1]
			print(f"[*] Peek Element - {peek}")

def main():
	stack = Stack(5,verbose=True)
	for i in range(1,6):
		stack.push(i)
	stack.printStack()
	stack.peek()
	stack.push(6)
	stack.printStack()
	for i in range(4):
		stack.pop()
	stack.printStack()
	stack.pop()
	stack.pop()



if __name__ == '__main__':
	main()

