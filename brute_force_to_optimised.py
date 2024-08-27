def subarraySum(nums, k):
    count = 0
  
    for start in range(len(nums)):
        current_sum = 0
        j = start
        while j < len(nums):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
            j += 1
    
    return count


def subarraySum(nums, k):
    count = 0
  
    for start in range(len(nums)):
        current_sum = 0
        for end in range(start, len(nums)):
            current_sum += nums[end]
            if current_sum == k:
                count += 1
    
    return count



def subarraySum(nums, k):   
    count = 0
    cumulative_sum = 0
    sum_dict = {0: 1}  # Initialize with 0 sum to handle cases where subarray starts from index 0
    
    for num in nums:
        cumulative_sum += num
        
        # Check if there is a subarray (ending at the current index) whose sum is k
        if (cumulative_sum - k) in sum_dict:
            count += sum_dict[cumulative_sum - k]
        
        # Update the cumulative sum frequency in the dictionary
        if cumulative_sum in sum_dict:
            sum_dict[cumulative_sum] += 1
        else:
            sum_dict[cumulative_sum] = 1
    
    return count
