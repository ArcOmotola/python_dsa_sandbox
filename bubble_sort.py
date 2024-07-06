# def bubble_sort(arr):
#   for i in range(len(arr)):
#     #track whether a swap was made on this pass
#     swapped = False
    


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

example_array = [2,0,2,1,1,0]
print(bubble_sort(example_array))
