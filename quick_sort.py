def quicksort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  smaller = [nums for nums in array[1:] if nums <= pivot]
  greater = [nums for nums in array[1:] if nums > pivot]
  return quicksort(smaller) + [pivot] + quicksort(greater)

print(quicksort([3, 5, 2, 9, 1, 8]))




# OR



def quicksort(array):
  if len(array) <= 1:
    return array
  
  mid_index = len(array) // 2
  pivot = array[mid_index]
  smaller = [nums for nums in array if nums < pivot]
  equal = [nums for nums in array if nums == pivot]
  greater = [nums for nums in array if nums > pivot]
  return quicksort(smaller) + equal + quicksort(greater)


print(quicksort([3, 5, 2, 9, 1, 8]))
