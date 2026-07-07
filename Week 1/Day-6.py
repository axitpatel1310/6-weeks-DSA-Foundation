#Maximum Sum Subarray of Size K
"""
class Solution:
    def max_sum_subarr(self,arr,k):
        n = len(arr)
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(k,n):
            window_sum = window_sum - arr[i-k] + arr[i]
            max_sum = max(max_sum,window_sum)            
        print(max_sum)            
sol = Solution()
sol.max_sum_subarr([1,2,3,5,6],2)                            
"""

#Longest Substring Without Repeating Characters (optimized)
"""
class Solution:
    def long_substring_no_rep(self,string):
        new = list(string)
        temp = []
        for i in new:
            if i in temp:
                break
            else:
                temp.append(i)
        return "".join(temp) 
sol = Solution()
print(sol.long_substring_no_rep("abcedfrr"))
"""

#Longest Repeating Character Replacement
"""
class Solution:
    def long_rep_char_rep(self, s, k):
        left = 0
        longest = 0
        max_freq = 0
        count = {}
        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            max_freq = max(max_freq, count[char])
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
sol = Solution()
print(sol.long_rep_char_rep("AABAAAAA",1))
"""

#Minimum Size Subarray Sum
"""
class Solution:
    def min_size_sub_sum(self, arr, target):
        left = 0
        total = 0
        min_length = float("inf")
        for right in range(len(arr)):
            # Expand the window
            total += arr[right]

            # Shrink the window while it satisfies the condition
            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= arr[left]
                left += 1
        if min_length == float("inf"):
            return 0
        return min_length
sol = Solution()
print(sol.min_size_sub_sum([1, 2, 3, 4, 5], 9))
"""
