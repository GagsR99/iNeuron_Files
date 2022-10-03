## Function Definition
def search2DArray(arr,target):
    m = len(arr)
    if m == 0:
        return False
    n = len(arr[0])
    left, right = 0, m*n-1
    

## Driver code
arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
result = search2DArray(arr,target)
print(result)
