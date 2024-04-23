class ListNode:
  def __init__(self, key = -1, value =  -1, next = None):
    self.key = key
    self.value = value
    self.next = next

class MyHashMap:
  def __init__(self):
    self.map = [ListNode() for _ in range(1000)]

  def hash(self, key):
    return key % len(self.map)
  
  def put(self, key, value):
    cur = self.map[self.hash(key)]
    while cur.next:
      if cur.next.key == key:
        cur.next.value = value
        return
      cur = cur.next
    cur.next = ListNode(key, value)

  def get(self, key):
    cur = self.map[self.hash(key)]
    while cur.next:
      if cur.next.key == key:
        return cur.next.value
      cur = cur.next
    return -1
    
  def remove(self, key):
    cur = self.map[self.hash(key)]
    while cur.next:
      if cur.next.key == key:
        cur.next = cur.next.next
        # cur.next = None
    return -1

        
      


  
  