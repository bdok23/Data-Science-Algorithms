'''
Binary search is an algorithm that looks for a value in a sorted array in less than constant time. 
Performance: O(log n)
'''
# Implementation below
def binary_search(arr, target):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        # check if the target is equal to the element at the midpoint
        if arr[mid] == target:
            return mid # element found
        # if the target is smaller, search the left half
        elif arr[mid] > target:
            high = mid - 1
        # if the target is larger, search the right half
        else:
            low = mid + 1
    return -1 # element not found

# example
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 6
result = binary_search(sorted_array, target_element)
print(result) # index of element














