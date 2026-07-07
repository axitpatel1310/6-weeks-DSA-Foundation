#Binary Search
"""
class Solution:
    def binary_search(self, arr, target):
        left = 0
        right = len(arr)-1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == target:
                print(mid)
                return
            elif target < arr[mid]:
                right -= mid
            elif target > arr[mid]:
                left += mid     
sol = Solution()
sol.binary_search([1,2,3,4,5,6],3)
"""

#Search Insert Position
"""
class Solution:
    def search_insert_pos(self, arr, value):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == value:
                return mid
            elif arr[mid] > value:
                right = mid - 1
            else:
                left = mid + 1
        return left
sol = Solution()
print(sol.search_insert_pos([1, 2, 2, 3, 5, 6], 4))
"""


#First Bad Version
"""
SECRET_FIRST_BAD = 4
def isBadVersion(version: int) -> bool:
    return version >= SECRET_FIRST_BAD
class Solution:
    def first_bad_version(self, n):
        left = 0
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left    
sol = Solution()
print(sol.first_bad_version(5))
"""