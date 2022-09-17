def two_pointer(arr, l, r, k):
    while l <= r:
        if arr[l] + arr[r] == k:
            return l,r
        elif arr[l] + arr[r] > k:
            r = r - 1
        else:
            l = l + 1
    return -1, -1

## Driver Code
arr = [20, 40, 60, 80, 90, 120, 240]
l = 0
r = len(arr) - 1
k = 210
left, right = two_pointer(arr, l, r, k)
print(arr[left], arr[right])