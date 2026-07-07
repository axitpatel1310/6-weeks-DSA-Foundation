#Two Sum (Sorted Array)

#Brute Force Solution
"""
class Solution:
    def two_sum(self, arr,target):
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i] + arr[j] == target:
                    return arr[i],arr[j]
sol = Solution()
print(sol.two_sum([3,4,5,7],9))       
"""

#Opposite Direction Pointers
"""
class Solution:
    def two_sum(self,nums,target):
        left = 0
        right = len(nums)-1
        while left < right:
            current = nums[left] + nums[right]            
            if current == target:
                return nums[left],nums[right]
            elif current < target:
                left += 1
            else:
                right -= 1
sol = Solution()
print(sol.two_sum([1,2,3,4,5,6],9))
"""

#Valid palindrome
"""
class Solution:
    def valid_palindrome(self, s):
        new = "".join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(new) - 1
        while left < right:
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1
        return True
sol = Solution()
print(sol.valid_palindrome("a man, a plan, a canal: panama"))
print(sol.valid_palindrome("racecar"))
print(sol.valid_palindrome("hello"))
"""

#Container With Most Water
"""
height = [1,8,6,2,5,4,8,3,7]
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            width = right - left
            current_height = min(height[left],height[right])
            area = width * current_height
            max_area = max(max_area,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1                
        return max_area
sol = Solution()
print(sol.maxArea(height))
"""

#Square of Sorted Array
"""
arr = [1,2,3,4,5,6]
class Solution:
    def sqr_sorted_arr(self,arr):
        for i in range(0,len(arr)):
            arr[i] = (arr[i])**2
        print(arr)
sol = Solution()
sol.sqr_sorted_arr(arr) 
"""