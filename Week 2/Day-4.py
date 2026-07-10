#Search in Rotated Sorted Array
"""
class Solution:
    def search_ele(self, arr, ele):
        for i in range(len(arr)):
            if arr[i] == ele:
                return i
        return "Not found"   
sol = Solution()
print(sol.search_ele([1,2,3,4,5,6],4))
"""

"""
class Solution:
    def search_ele(self,arr,ele):
        left = 0
        right = len(arr)-1
        while left < right:
            mid = (left + right)//2
            if arr[mid] == ele:
                return mid
            elif arr[mid] < ele:
                left = mid + 1
            else:
                right = mid - 1
sol = Solution()
print(sol.search_ele([1,2,3,4,5,6,8],6)) 
"""                

#Find Minimum in Rotated Sorted Array
"""
class solution:
    def find_min(self,arr):
        left = 0
        right = len(arr)-1
        while left < right:
            mid = (right+left) // 2
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        return f"Element: {arr[left]} at Index: {left}" 
sol = solution()
print(sol.find_min([2,3,4,5,6,0,1]))
"""

#Search in Rotated Sorted Array II (duplicates)
"""
class Solution:
    def search_rot_sort_arr(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return True
            if arr[left] == arr[mid] == arr[right]:
                left += 1
                right -= 1
            elif arr[left] <= arr[mid]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
sol = Solution()
print(sol.search_rot_sort_arr([2, 5, 6, 0, 0, 1, 2], 0))  
"""

#Rotation Count of an Array
"""
class solution:
    def rotation_count(self,arr):
        left = 0
        right = len(arr)-1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        return left
sol = solution()
print(sol.rotation_count([1,2,3,4,5,1,2,3,4,5,1,2]))
"""