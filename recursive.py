def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

def array_len(arr):
    if arr == []:
        return 0;
    return 1+array_len(arr[1:])

def max(arr):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0]>arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    def dfs(left,right):
        mid  = (left + right)//2
        if left > right :
            return -1 
        if arr[mid]>target:
            return dfs(left,mid-1)
        elif arr[mid] < target:
            return dfs(mid+1,right)
        else:
            return mid
    return dfs(left,right) 

