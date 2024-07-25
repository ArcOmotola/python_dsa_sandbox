
# IN-ORDER TRAVERSAL - RECURSIVELY
def in_order_traversal(node, result):
  if node:
    in_order_traversal(node.left, result)
    result.append(node.value)
    in_order_traversal(node.right, result)
    
    
# IN-ORDER TRAVERSAL - ITERATIVELY
def in_order_traversal_iterative(root):
  result = []
  stack = []
  
  current = root
  
  while stack or current:
    while current:
      stack.append(current)
      current = current.left
    current = stack.pop()
    result.append(current.value)
    current = current.right
    
  return result



# PRE-ORDER TRAVERSAL - RECURSIVELY
def pre_order_traversal(node, result):
  if node:
    result.append(node.value)
    pre_order_traversal(node.left, result)
    pre_order_traversal(node.right, result)

# PRE-ORDER TRAVERSAL - ITERATIVELY
def pre_order_traversal_iterative(root):
  result = []
  stack = [root]
  
  while stack:
    node = stack.pop()
    if node:
      result.append(node.value)
      result.append(node.right)
      result.append(node.left)
  return result



# POST-ORDER TRAVERSAL - RECURSIVELY

def post_order_traversal(node, result):
  if node:
    post_order_traversal(node.left, result)
    post_order_traversal(node.right, result)
    result.append(node.value)
    


def post_order_traversal_iterative(root):
  if not root:
    return []
  
  stack1 = [root]
  stack2 = []
  
  while stack1:
    node = stack1.pop()
    stack2.append(node)
    if node.left:
      stack1.append(node.left)
    if node.right:
      stack1.append(node.right)
  return [node.value for node in reversed(stack2)]
  
  
  
# BREADTH-FIRST SEARCH (BFS) TRAVERSAL
from collections import deque

def level_order_traversal(root):
  result = []
  
  if not root:
    return result
  
  queue = deque([root])
  
  current = root