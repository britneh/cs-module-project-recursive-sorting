# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    #pre allocating our output array with the number of elements 
    #we know it will hold at the end
    merged_arr = [0] * elements

    # init pointers to the beginning of arrA and arrB
    a = 0
    b = 0
    #compare the elements those pointers are pointing at
    #whichever element is less than or equal
    #loop so long as both pointers are in range of their respective arrays
    for i in range(elements):
        #push that element to the output arr
        if a >= len(arrA):
            #we've moved all the elements from arrA into merged_arr
            #we still have elements from arrB that need to be moved
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1


        #increment the pointer pointing to the element we just pushed to the output array 
#Now only one of the pointer is in range of its array, in other words we'e moved all elements 
#from one array to the output array and we need to move al of the elems of the other 
# array to the output array

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len (arr) > 1:
       left = merge_sort(arr[0: len(arr) // 2])
       right = merge_sort(arr[len(arr) //2 :])
       arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

