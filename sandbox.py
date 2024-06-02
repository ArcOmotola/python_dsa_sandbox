


map_store = {}
word = "aggyuufjlgke"

for i in range(len(word)):
  map_store.setdefault(word[i], 0)
  map_store[word[i]] += 1

print(map_store)
  



















# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_length = 0
#         visited = set()
#         l = 0
#         r = 0

#         while r < len(s):
#             if s[r] not in visited:
#                 visited.add(s[r])
#             max_length = (max_length, r - l + 1)
                
#             else:
#                 l = r
#                 visited.clear()
#                 visited.add(s[r])
                

#             r += 1

#         return max_length