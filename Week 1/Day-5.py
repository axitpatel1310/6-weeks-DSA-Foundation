#Longest Consecutive sequence
"""
class Solution:
    def long_conseq(self, nums):
        current = nums[0]
        count = 0
        for i in nums:
            if i == current:
                count += 1
            else:
                current = i
        return count
sol = Solution()
print(sol.long_conseq([1,2,3,4,5,5,5]))
"""

#Top K Frequent Elements
"""
class Solution:
    def top_k_ele(self,nums,k):
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        arr = list(freq.items())
        n = len(arr)
        for i in range(n):
            max_idx = i
            for j in range(i+1,n):
                if arr[j][1] > arr[max_idx][1]:
                    max_idx = j
            arr[i],arr[max_idx] = arr[max_idx],arr[i]
            result = []
            for i in range(k):
                result.append(arr[i][0])
        return result        
sol = Solution()
print(sol.top_k_ele([1,2,3,3,4,4,4,4],3))
"""

#Subarray Sum Equals K
"""
class Solution:
    def subarray_sum_k(self,array,target):
        for i in range(len(array)):
            current_total = 0
            list = []
            for j in range(i, len(array)):
                current_total += array[j]
                list.append(array[j])
                if current_total == target:
                    return list
        return []           
sol = Solution()
print(sol.subarray_sum_k([1,2,3,4,5,6],9))
"""

#Longest Substring Without Repeating Characters
"""
class Solution:
    def long_sub_no_rep(self, string):
        longest = ""
        for i in range(len(string)):
            seen = ""
            for j in range(i, len(string)):
                if string[j] in seen:
                    break
                seen += string[j]
            if len(seen) > len(longest):
                longest = seen
        return longest
sol = Solution()
print(sol.long_sub_no_rep("helaaroooo"))                
"""