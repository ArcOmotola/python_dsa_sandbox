# import json

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

#     def add_child(self, child_node):
#         self.children.append(child_node)

# def fetch_all_nodes(node, parent_value=None):
#     nodes = []
#     node_dict = {
#         'value': node.value,
#         'parent': parent_value,
#         'children': []
#     }
#     for child in node.children:
#         node_dict['children'].append(child.value)
#         nodes.extend(fetch_all_nodes(child, node.value))
#     nodes.append(node_dict)
#     return nodes

# def tree_to_json(tree):
#     nodes = fetch_all_nodes(tree)
#     return json.dumps(nodes, indent=4)

# if __name__ == "__main__":
#     # Create sample tree
#     root = TreeNode('root')
#     child1 = TreeNode('child1')
#     child2 = TreeNode('child2')
#     grandchild1 = TreeNode('grandchild1')
#     grandchild2 = TreeNode('grandchild2')

#     root.add_child(child1)
#     root.add_child(child2)
#     child1.add_child(grandchild1)
#     child2.add_child(grandchild2)

#     # Get JSON representation of the tree
#     tree_json = tree_to_json(root)
#     print(tree_json)




# # [
# #     {
# #         "value": "grandchild1",
# #         "parent": "child1",
# #         "children": []
# #     },
# #     {
# #         "value": "child1",
# #         "parent": "root",
# #         "children": [
# #             "grandchild1"
# #         ]
# #     },
# #     {
# #         "value": "grandchild2",
# #         "parent": "child2",
# #         "children": []
# #     },
# #     {
# #         "value": "child2",
# #         "parent": "root",
# #         "children": [
# #             "grandchild2"
# #         ]
# #     },
# #     {
# #         "value": "root",
# #         "parent": null,
# #         "children": [
# #             "child1",
# #             "child2"
# #         ]
# #     }
# # ]

def convert(s: str, numRows: int) -> str:
    # Edge cases
    if numRows == 1 or numRows >= len(s):
        return s
    
    # Initialize a list to hold strings for each row
    rows = [''] * numRows
    
    # Variables to track the current row and direction
    current_row = 0
    going_down = False
    
    # Iterate through each character in the string
    for char in s:
        # Add the character to the current row
        rows[current_row] += char
        
        # Change direction if we are at the top or bottom row
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        
        # Move to the next row
        current_row += 1 if going_down else -1
    
    # Combine all rows to get the final string
    return ''.join(rows)

# Example usage
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"









import heapq

# Create an array
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Convert array to a heap
heapq.heapify(array)

print("heaped>>>", array)

min_element = heapq.heappop(array)

# print("smallest>>>", min_element)
# min_element = heapq.heappop(array)

# print("smallest>>>", min_element)
# min_element = heapq.heappop(array)
# print("heaped>>>", array)
# min_element = heapq.heappop(array)
# print("heaped>>>", array)
# min_element = heapq.heappop(array)
# print("heaped>>>", array)
# min_element = heapq.heappop(array)


# # Add a new element
# heapq.heappush(array, 0)

# # Remove and return the smallest element
# min_element = heapq.heappop(array)

# print("Updated heap after push and pop:", array)
# print("Removed element:", min_element)


def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
            
test_arr = [2,0,2,1,1,0]
sortColors(test_arr)
print(test_arr)





from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        visited = set()
        temp_sum = 0
        max_sum = 0

        l = 0
        r = 0

        # Initialize the first window of size k
        for r in range(k):
            visited.add(nums[r])
            temp_sum += nums[r]

        # After the initial window setup
        max_sum = temp_sum if len(visited) == k else 0
        
        # Start sliding the window
        while r < len(nums):
            # Remove the element going out of the window from the sum and set
            temp_sum -= nums[l]
            visited.remove(nums[l])
            l += 1

            if r < len(nums):
                # Add the new element into the window sum and set
                temp_sum += nums[r]
                visited.add(nums[r])
                r += 1

            # Update max_sum if we have k distinct elements in the window
            if len(visited) == k:
                max_sum = max(temp_sum, max_sum)

        return max_sum

# Example usage
solution = Solution()
print(solution.maximumSubarraySum([1, 2, 3, 4, 5, 6], 3))  # Output should be the sum of any window of size 3 where all elements are distinct



test_word = "9392"
print("+++++", test_word.isdigit())





def customSortString(self, order: str, s: str) -> str:
    # Create a hashmap to count occurrences of each character in s
    hash_map = {item: s.count(item) for item in s}
    res = ""
    hash_rem_word = ""

    # Iterate over characters in the order string
    for char in order:
        if char in hash_map:
            res += char * hash_map[char]
            del hash_map[char]

    # Append the remaining characters from the hashmap
    for key, value in hash_map.items():
        hash_rem_word += key * value

    return res + hash_rem_word


# print("r" * 0)