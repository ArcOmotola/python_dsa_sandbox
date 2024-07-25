def reverseWords(s):
    # Helper function to reverse a portion of the list
    def reverse(left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    # Step 1: Reverse the entire list
    reverse(0, len(s) - 1)
    
    # Step 2: Reverse each word in the list
    start = 0
    for end in range(len(s)):
        if s[end] == ' ':
            reverse(start, end - 1)
            start = end + 1
    # Reverse the last word
    reverse(start, len(s) - 1)
    
    
    
# Example usage:

def reverseString(s):
    l = 0
    r = len(s) - 1
    
    while l <= r:
        s[r], s[l] = s[l], s[r]
        l += 1
        r -= 1
        
word = ["h"]
reverseString(word)

print(word)
        


number = "omotolamide"
res = number[::-1]

print(res)


        
        
s = "3322251"

# ans = [item for item in s]

ans = sorted("eat")

print(ans)
    
strs = ["flower","flow","flight"]

print(min(strs, key=len))

s = "omotola"
t = "omatolo"

char_frequency_s = {char:s.count(char) for char in set(s)}
char_frequency_t = {char:t.count(char) for char in set(t)}


print(char_frequency_s)
print(char_frequency_t)

print("debug>>>", char_frequency_t == char_frequency_s)
print({"l": 4, "h": 7} == {"l": 8, "h": 7})

test1 = [4, 5, 6] + [9]
ans = [str(i) for i in test1]
print(" ".join(ans))


def test(m):
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            print("O(n^2)>>>", m[i] + m[j])
            

test([2,7,9,6,8,5])


def test(m):
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            for k in range(j+1, len(m)):
                print("O(n^3)", m[i] + m[j] + m[k])
            

test([2,7,9,6,8,5])



def compress(chars):
    res = []

    if len(chars) == 1:
        return chars

    counter_map = {char:chars.count(char) for char in chars}

    # {"a":3, "b":5, "c":1, "d": 12}


    for char in counter_map:
        if counter_map[char] == 1:
            res.append(char)
        elif counter_map[char] >= 10:
            res.append(char)
            res.append(counter_map[char]//10) 
            res.append(counter_map[char]%10) 
        else:
            res.append(char)
            res.append(counter_map[char])

    return len(res)


print(compress(["a","a","b","b","c","c","c"]))

word = "  The sky is blue  "
word.strip()
new_word = word.split()
new_word.reverse()
res = " ".join(new_word)
# word_s = word.split()
# word_s.reverse()


print(res)
    
    
# def reverseWords(str):
#     word = str.split()
#     new_word = word.reverse()
    

#     res = " ".join(new_word)
    
#     return res
    
    

# print("+++++++", reverseWords(word))

word_W = "  The sky is blue  "

def reverseWords(s):
    s.strip()
    words = s.split()
    res=''
    for i in range(len(words)-1,-1 ,-1):
            res += words[i] + " "
    return res.strip()

print(reverseWords(word_W))




# def reverseWords(S):
#     s_list = s.split(" ")
#     ans = ""
#     for i in s_list[::-1]:
#         if i == "":
#             continue
#         else:
#             ans = ans + " " + i

#     return ans.strip()


read = "a good   example"
read.strip()
text = read.split()

print(text)

p = "toddler"
bucket = sorted("methaphor is the word")
print(bucket)



def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0

    n, h = len(needle), len(haystack)
    
    l = 0  # start of the current window
    r = 0  # end of the current window
    p = 0  # current position in needle
    
    while r < h:
        if haystack[r] == needle[p]:
            r += 1
            p += 1
            
            if p == n:
                return l
        else:
            l += 1
            r = l
            p = 0
    
    return -1




        # if len(s) == 0:
        #     return True 

        # s.strip()
        # s.lower()

        # new_word = ""

        # for char in s:
        #     if char.isalnum():
        #         new_word += char

        # l = 0
        # r = len(new_word) - 1

        # while l < r:
        #     if new_word[l] != new_word[r]:
        #         return False
        #     l += 1
        #     r -= 1

        # return True
        
ans = "word for the wise".split()

# ans[]

print(">>>>>>>>>", ans)

def generate_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    return substrings

# Example usage
# s = "tola"
# substrings = generate_substrings(s)
# print("All substrings of '{}':".format(s))
# for substring in substrings:
#     print(substring)
    
    
    

