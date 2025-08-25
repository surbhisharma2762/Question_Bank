class Solution:
    def findMajority(self, arr):
        n = len(arr)
        if n == 0:
            return []
        v_count = {}
        for vote in arr:
            v_count[vote] = v_count.get(vote, 0) + 1
        result = []
        threshold = n / 3
        for candidate, count in v_count.items():
            if count > threshold:
                result.append(candidate)
        return sorted(result)

# Test the function
arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
obj = Solution()
print(obj.findMajority(arr))  # Output: [5, 6]
