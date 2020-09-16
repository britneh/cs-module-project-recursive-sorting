# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    
    if start > end:
        return -1
    else:
        mid = (start + end)// 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid -1)
        else:
            return  binary_search(arr, target, mid +1, end)

chance = [15, 21, 47, 84, 96]
print(binary_search(chance, 84, 0, 5))



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

