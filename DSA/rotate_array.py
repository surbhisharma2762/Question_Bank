class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n
        arr[:] = arr[d:] + arr[:d]
        return arr

# Test the function
sol = Solution()
arr = [1, 2, 3, 4, 5]
d = 2
sol.rotateArr(arr, d)
print("Rotated array:", arr)
