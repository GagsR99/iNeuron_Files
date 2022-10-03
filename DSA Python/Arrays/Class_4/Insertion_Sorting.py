<<<<<<< HEAD
# Implementation
# Time Complexity : O(n^2)
def insertSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr

# Driver Code
arr = [75,85,90,100,80,95]
result = insertSort(arr)
=======
# Implementation
# Time Complexity : O(n^2)
def insertSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr

# Driver Code
arr = [75,85,90,100,80,95]
result = insertSort(arr)
>>>>>>> ac53ea002a8985ae21c38d58bd2e9ce7ace7d3be
print(result)