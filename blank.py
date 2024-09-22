print(ord("a"))
s = "source"
t = "sources"


arr1 = [0] * 6
print("arr", arr1)


print("re" * 2)


# print("".join(["4,3,8,8,1", "omotee", "ogunsola"]))

word = "omotola#ogunsola*is#jumpimg"
print(word.split("#"))

word2 = "omotola"
print(word2.split("#"))


import re

string = "apple;banana,cherry orange+mango"
array = re.split(r'[;,+ ]', string)
print(array)


test_input = "anagram"

def tester(word_3):
  hash_map = {}
  
  for i in range(len(word_3)):
    hash_map[word_3[i]] = 1 + hash_map.get(word_3[i], 0)
    
  return hash_map
    

print("degug>>", tester(test_input))



word_list = ["footer", "foo", "footed", "fooooo"]
result = sorted(word_list)

print("sort_debug>>", result)


arr_test = [2, 5, 0, 4, 1, 9]
print("int_sort_debug>>", sorted(arr_test, key=lambda x: -x))


test_arr_3 = [[8,7],[9,9], [9,10],[7,4],[9,7]]
test_arr_3.sort()

print((test_arr_3))



print([[0] * 4] * 3)





























# def encode(strs) -> str:
#     res = ""
#     for s in strs:
#         res += str(len(s)) + "#" + s
#     return res
  
# # 5#Hello7#World
# def decode(s):
#   res = []
#   l = 0
#   r = 0
#   while r < len(s):
#     while (s[r]).isalpha():
#       r += 1
      
    
    
#     res.append()

# print(encode(["Hello","World"]))


# # arr = ['Omotola', 'Ogunsola']
# # word = "Omotola Ogunsola"
# # print(" ".join(arr))
# # print(word.split())


# hash_map = {"a":3, "b": 5}
# temp = hash_map

# print(temp)