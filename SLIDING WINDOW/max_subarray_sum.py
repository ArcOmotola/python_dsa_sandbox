def max_sum_subarray(arr, k):
    # Check if k is greater than the array length
    if k > len(arr):
        return "Subarray size 'k' is larger than the array length."

    # Initialize the sum of the first 'k' elements
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Start the window from the k-th element and slide to the right
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]  # Slide the window: remove the element going out, and add the new element
        max_sum = max(max_sum, window_sum)  # Update the max sum found so far

    return max_sum
