class Array:
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.data = [None] * capacity

	def get(self, index):
		if index < 0 or index >= self.size:
			return None
		return self.data[index]

	def push(self, value):
		if self.size >= self.capacity:
			return False
		self.data[self.size] = value
		self.size += 1
		return True
	
	def pop(self):
		if self.size <= 0:
			return None
		popped_data = self.data[self.size - 1]
		self.data[self.size - 1] = None
		self.size -= 1
		return popped_data
	
	def delete(self, index):
		if index < 0 or index  >= self.size:
			return False
		for i in range(index, self.size - 1):
			self.data[i] = self.data[i + 1]
		self.data[self.size - 1] = None
		self.size -= 1
		return True
	
	def print_array(self):
		print(self.data[ : self.size])
		


# ////////////////////////////////////////////////////////////////
		
arr = Array(5)
arr.push(1)
arr.push(2)
arr.push(3)
arr.print_array()  # Output: [1, 2, 3]
print(arr.get(1))  # Output: 2
arr.pop()
arr.print_array()  # Output: [1, 2]
arr.delete(0)
arr.print_array()  # Output: [2]