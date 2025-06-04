class Solution:
    def moveZeroes(self,arr):
        pos = 0
        for num in arr:
            if num != 0:
                arr[pos] = num
                pos += 1
        arr[pos:] = [0] * (len(arr) - pos)
        return arr

# Test the function
arr = [0, 1, 0, 3, 0, 5]
obj = Solution()
print(obj.moveZeroes(arr))
