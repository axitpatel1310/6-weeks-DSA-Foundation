#First Occurance
"""
class Solution:
    def find_first_occ(self,arr,ele):
        left = 0
        right = len(arr)-1
        ans = -1        
        while left <= right:
            mid = left + (right - left)//2
        
            if arr[mid] == ele:
                ans = mid
                right = mid - 1
            elif arr[mid] < ele:
                left = mid + 1
            else:
                right = mid - 1
        return ans
sol = Solution()
print(sol.find_first_occ([1,2,3,4,5],4))
"""

"""
class Solution:
    def first_occ(self,arr,ele):
        for i in range(len(arr)):
            if arr[i] == ele:
                return i
sol = Solution()
print(sol.first_occ([1,2,3,4,5],4))
"""

#Last occurance
"""
class Solution:
    def last_occ(self,arr,ele):
        left = 0
        right = len(arr)-1
        ans = -1
        while left <= right:
            mid = left + (right - left)//2
            if arr[mid] == ele:
                ans = mid
                left = mid + 1
            if arr[mid] < ele:
                left = mid + 1
            else:
                right = mid - 1
        return ans
sol = Solution()
print(sol.last_occ([1,2,2,3,4,5],2))
"""

#Peak Element
"""
class solution:
    def peak_element(self,arr):
        left,right = 0, len(arr)-1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid
        return arr[left]
sol = solution()
print(sol.peak_element([1,2,3,4,6,2]))
"""

#Floor and Ceil
"""
class Solution:
    def floor_and_ceil(self,arr,target):
        left,right = 0,len(arr)-1
        while left < right:
            mid = (left + right)//2
            if arr[mid] == target:
                left = mid - 1
                right = mid + 1
                return arr[left], arr[right]
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
sol = Solution()
print(sol.floor_and_ceil([1,2,3,4,5,6,7],4))
"""