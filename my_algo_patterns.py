arr = [1, 2, 3]
res = []

for num in arr:
  res.extend([num] * num)  # Efficiently create sublists using extend

print(res)  # Output: [[1], [2, 2], [3, 3, 3]]


# ////////////////////////////////////////////////////////////////



map_store = {}
word = "aggyuufjlgke"

for i in range(len(word)):
  map_store.setdefault(word[i], 0)
  map_store[word[i]] += 1

print(map_store)



# ////////////////////////////////////////////////////////////

map_store = {}
word = "aggyuufjlgke"

for char in word:
    if char in map_store:
        map_store[char] += 1
    else:
        map_store[char] = 1

print(map_store)
