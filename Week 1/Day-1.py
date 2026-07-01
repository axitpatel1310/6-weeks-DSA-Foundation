#Arrays

#1. Find maximum element
"""
arr = [3,7,2,9,5]
class Solution:
    def find_max(self,nums):
        max = 0
        for i in nums:
           if i > max:
               max = i 
        print(max)
sol = Solution()
sol.find_max(arr)
"""
# Find the minimum element
"""
arr = [2,3,4,5,1,6,7]
class Solution:
    def findMin(self, nums):
        min = arr[0]    
        for i in nums:
            if i < min:
                min = i
        print(min)
sol = Solution()
sol.findMin(arr)
"""

#Sum of array
"""
arr = [2,3,5,3,2,5,6]
class Solution:
    def sum_of_array(self,nums):
        total = 0
        for i in nums:
            total += i
        print(total)
sol = Solution()
sol.sum_of_array(arr)
"""

#Count Even Numbers
"""
arr = [1,2,3,4,5,6,7,8]
class Solution:
    def count_even(self,nums):
        count = 0
        for i in nums:
            if i % 2 == 0:
                count += 1
        print(count)
sol = Solution()
sol.count_even(arr)
"""

#Reverse an array
"""
arr = [1,2,3,4,5,6]
class Solution:
    def reverse_array(self, nums):
        left  = 0
        right = len(nums) - 1
        while left < right:
            arr[left], arr[right] = arr[right],arr[left]
            left += 1
            right -= 1 
        print(arr)
sol = Solution()
sol.reverse_array(arr)
"""

#Check if array is sorted 
"""
arr = [1,2,3,4,7,2]
class Solution:
    def check_sorted(self,arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
sol = Solution()
print(sol.check_sorted(arr))
"""

#Second largest element
"""
arr = [5,2,3,7,6,9]
class Solution:
    def second_largest(self,nums):
        largest = arr[0]
        second = arr[0]
        for i in nums:
            if i > largest:
                second = largest
                largest = i
            elif i > second and i != largest:
                second = i
        print(second)       
sol = Solution()
sol.second_largest(arr)         
"""

#Remove Duplicates from Sorted Array
"""
arr = [1,2,3,4,5,6,6,7,8]
class Solution:
    def remove_duplicates(self,arr):
        ele = []
        for i in arr:
            if i in ele:
                arr.pop(i)
                break
            ele.append(i)    
        print(arr)
sol = Solution()
sol.remove_duplicates(arr)
"""

#Move All zeros to the end
"""
arr = [0,1,0,3,4,5]
class Solution:
    def move_zeros(self,arr):
        j = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[j] = arr[i]
                j += 1
        while j < len(arr):
            arr[j] = 0 
            j += 1
        print(arr)
sol = Solution()
sol.move_zeros(arr)
"""

#Rotate array by one position
"""
arr = [1,2,3,4,5,6]
class Solution:
    def rotate_one(self,arr,pos):
        last = arr[-1]
        
        for i in range(len(arr)-1,pos,-1):
            arr[i] = arr[i-1]
        
        arr[pos] = last
        print(arr)

sol = Solution()
sol.rotate_one(arr,3)
"""