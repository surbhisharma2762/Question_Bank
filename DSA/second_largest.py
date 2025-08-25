class Solution:
    def getSecondLargest(self, arr):
        first = second = float('-inf')
        for num in arr:
            if num > first: 
                second, first = first, num
            elif first > num > second:
                second = num
        return second if second != float('-inf') else -1

# Example usage
arr = [4, 7, 1, 7, 3]
obj = Solution()
print(obj.getSecondLargest(arr))  # Output: 4
