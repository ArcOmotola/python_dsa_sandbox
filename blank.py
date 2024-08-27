def checkSubarraySum(nums):
  prefixSum = [0] * (len(nums) + 1)
  for i in range(1, len(nums) + 1):
        prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
      
  
  return prefixSum
      
print(checkSubarraySum([4, 6, 3, 1, 6, 0]))




print(%5) 