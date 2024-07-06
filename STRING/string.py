s = "()[]{}"

copy = s.split()

# j = "+"

# new_string = " ".join(copy)

print(copy)
# print(new_string)



  #  def reverseWords(self, s: str) -> str:
  #       j = s.split(' ')
  #       res = ""
  #       for i in j:
  #           if i == '':
  #               continue
  #           res = i + ' ' + res

  #       return res[:-1]
  
  
#   class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for char in s:
#             if char == '{':
#                 stack.append('}')
#             elif char == '(':
#                 stack.append(')')
#             elif char == '[':
#                 stack.append(']')
#             else:
#                 if not (stack and stack.pop() == char):
#                     return False
#         return False if stack else True
      
      
      
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         pairs = { '(': ')',
#         '[': ']',
#         '{': '}'
#         }
#         for char in s:
#             if char in pairs:
#                 stack.append(char)
#             elif len(stack) == 0 or char != pairs[stack.pop()]:
#                 return False
#         return len(stack) == 0









class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = (0, 0)
        for i in range(n):
            dp[i][i] = True
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = (i,i+1)
        for diff in range(2, n):
            for i in range(n - diff):
                if s[i] == s[i + diff] and dp[i + 1][i + diff - 1]:
                    dp[i][i + diff] = True
                    ans = (i, i + diff)
        i, j = ans
        return s[i : j + 1]







# def groupAnagrams(strs):
    # res = defaultdict(list)  #mapping charCount to list the Anagrams

    # for s in strs:
    #     count = [0] * 26

    #     for c in s:
    #         count[ord(c) - ord("a")] += 1

    #     res[tuple(count)].append(s)

    # return res.values()


def convert_list_to_int(digits):
  """Converts a list of digits to an integer.

  Args:
      digits: A list of integers representing the digits of the number.

  Returns:
      The integer formed by the digits.
  """
  number = 0
  for i, digit in enumerate(digits):
    number += digit * (10 ** (len(digits) - i - 1))
  return number

def convert_int_to_list(number):
  """Converts an integer to a list of digits.

  Args:
      number: The integer to be converted.

  Returns:
      A list of digits representing the integer.
  """
  digits = []
  while number > 0:
    digit = number % 10
    digits.append(digit)
    number //= 10
  return digits[::-1]  # Reverse the list to get the correct order

# Example usage
digits = [3, 2, 0, 4, 9]
integer = convert_list_to_int(digits)
print(integer)  # Output: 32049

new_digits = convert_int_to_list(integer)
print(new_digits)  # Output: [3, 2, 0, 4, 9]





# convert [3,2,0,4,9] to an integer 32049 and back to an array


# ////////////////////////////////////////////////////////////////


def plusOne(digits):
    # Convert the list of digits into a single integer
    number = int("".join(map(str, digits)))
    
    # Increment the integer
    number += 1
    
    # Convert the incremented integer back to a list of digits
    return [int(digit) for digit in str(number)]
  
  
  
def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    # postfix = 1
    # for i in range(len(nums) - 1, -1, -1):
    #     res[i] *= postfix
    #     postfix *= nums[i]
    
    return res
  

print(productExceptSelf([1,2,3,4]))

nums = [5, 7, 3, 2, 5, 9, 4, 2]

print("maximu_number>>", [nums[i] for i in range(len(nums))])





# Python3 code for the above approach

# function to find the length of longest
# subarray having sum k
def lenOfLongSubarr(arr, N, K):
  
    # Variable to store the answer
    maxlength = 0

    for i in range(0,N):

        # Variable to store sum of subarrays
        Sum = 0
        
        # if maximum possible subarray length from i is equal to maxLength
        if (maxlength == N - i):
              break
            
        for j in range(i,N):

            # Storing sum of subarrays
            Sum += arr[j]

            # if Sum equals K
            if (Sum == K):

                # Update maxLength
                maxlength = max(maxlength, j - i + 1)

    # Return the maximum length
    return maxlength

# Driver Code
# Given input
arr = [ 10, 5, 2, 7, 1, 9 ]
n = len(arr)
k = 15

# Function Call
print("Length = " , lenOfLongSubarr(arr, n, k))

# This code is contributed by akashish__




