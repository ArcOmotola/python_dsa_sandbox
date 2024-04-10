class MyHashSet:

  def __init__(self):
    self.data = []

  def add(self, key):
    if key not in self.data:
      self.data.append(key)

  def remove(self, key):
    if key in self.data:
      self.data.remove(key)

  def contains(self, key):
    return key in self.data


# Driver code
hash_set = MyHashSet()

hash_set.add(5)
hash_set.add(3)
hash_set.add(7)
hash_set.add(1)
hash_set.add(9)

hash_set.remove(3)

print(hash_set.contains(7))


print(hash_set.data)

# TIME AND SPACE COMPLEXITY

"""
This implementation has linear time complexity for both adding and removing elements (O(n)), 
where n is the number of elements in the hash set. The contains operation also has linear time 
complexity (O(n)), as it needs to traverse the list to check for the presence of the element.

While this implementation works, it may not be efficient for scenarios with a large number of 
elements, especially when searching for elements. In such cases, using a more efficient data 
structure like a hash table or Python's built-in set would be preferable.
"""


# ////////////////////////////////////////////////////////////////


# IMPLEMENTATION USING HASHTABLE
class MyHashSetHashtable:
  def __init__(self):
    self.size = 100 # size of the hashtable (can be adjusted)
    self.table = [[] for _ in range(self.size)]

  def _hash_function(self, key):
    return key % self.size
  
  def add(self, key):
    hash_key = self._hash_function(key)
    if key not in self.table[hash_key]:
      self.table[hash_key].append(key)

  def remove(self, key):
    hash_key = self._hash_function(key)
    if key in self.table[hash_key]:
      self.table[hash_key].remove(key)

  def contains(self, key):
    hash_key = self._hash_function(key)
    return key in self.table[hash_key]

  
""" 
Overall, the time complexity for each operation is generally O(1) on average, assuming good 
hashing behavior. However, in the worst case, it can be O(N) if there are many collisions, although 
this is mitigated by using techniques such as chaining (as in this implementation).
"""

hash_set = MyHashSetHashtable()

hash_set.add(1)
hash_set.add(2)
hash_set.add(3)

print("After adding elements:", hash_set.table)

hash_set.remove(2)

print("After removing 2:", hash_set.table)

print("Does it contain 1?", hash_set.contains(1))
print("Does it contain 2?", hash_set.contains(2))


# ////////////////////////////////////////////////////////////////





  

















