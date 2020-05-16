'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
'''

class Node:
	def __init__(self, val):
		self.val = val
		self.both = 0

	def __str__(self):
		return str(self.val)

class XORLinkedList:

	def __init__(self, arg):
		self.head = Node(None)
		self.tail = Node(None)

	def add(element):
		newNode = Node(element)
		if self.head == None:
			self.head = self.tail = newNode
		else:
			newNode.both = get_pointer(self.tail)
			self.tail.both = self.tail.both ^ get_pointer(newNode)
			self.tail = newNode

	def get(index):
		previousAddr = 0
		current = self.head
		if i in range(0,index-1):
			temp = get_pointer(current)
			current = dereference_pointer(previousAddr^current.both)
			previousAddr = temp
			if current.both == previousAddr and i > index - 2:
				return None
		return current
