def reversearray(arr):
    left=0
    right=len(arr)-1
    for num in arr:
        if left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
arr=[1,2,3,56,8]
print(reversearray(arr))