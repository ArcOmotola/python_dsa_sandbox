# creates all substring
def test_func(sword):
    res = []
    for l in range(len(sword)):
        for r in range(l + 1, len(sword) + 1):
            res.append(sword[l:r])
    return res

print("test_func)))))",test_func("tola"))



p = "mayowa"

def countSubstrings(s):
  counter = 0
  subString = ""

  if len(s) == 1:
      return 1
  
  if not s:
      return 0

  def isPalindrome(word):
      l = 0
      r = len(word) - 1

      while l < r:
          if word[l] != word[r]:
              return False
          
          l += 1
          r -= 1
      return True


  # l = 0
  # r = 1
  # while l >= 0 and r < len(s):
  #     if isPalindrome(s[l:r]):
  #         count
  #         l

  count = 1
  p = 0
  l = p - 1
  r = p + 1

  while p < len(s) - 1:
      if p > 0:
          count += 1
          while l > 0 and r < len(s) and isPalindrome(s[l:r]):
              l -= 1
              r += 1
              count += 1
  
  return count



print("solution>>>>>>",countSubstrings("omotola"))






# # Constants for 32-bit signed integer range
#         INT_MAX = 2**31 - 1
#         INT_MIN = -2**31

#         # Step 1: Ignore leading whitespace
#         s = s.strip()

#         # Step 2: Check if the string is empty after trimming
#         if not s:
#             return 0

#         result = ""
#         no_digit_exists = True
#         sign = 1  # Default to positive

#         i = 0
#         # Step 3: Determine the sign
#         if s[0] in ["+", "-"]:
#             if s[0] == "-":
#                 sign = -1
#             i += 1

#         # Step 4: Read the digits and form the integer
#         for char in s[i:]:
#             if not char.isdigit():
#                 break

#             if char == "0" and no_digit_exists:
#                 continue

#             no_digit_exists = False
#             result += char

#         if no_digit_exists or result == "":
#             return 0

#         # Step 5: Convert the result string to integer and apply the sign
#         result = sign * int(result)

#         # Step 6: Handle overflow by rounding to the 32-bit signed integer range
#         if result < INT_MIN:
#             return INT_MIN
#         if result > INT_MAX:
#             return INT_MAX

#         return result