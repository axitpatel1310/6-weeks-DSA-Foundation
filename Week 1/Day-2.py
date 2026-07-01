#Find missing number
"""
class Solution:
    def find_miss(self, nums):
        for i in range(len(nums)-1):    
            if nums[i]+1 != nums[i+1]:
                return True
        return False
arr = [1,2,3,4,5,6,7,8]
sol = Solution()
print(sol.find_miss(arr))
"""

#Contains Duplicate
"""
class Solution:
    def cont_dup(self,nums):
        dup_list = []
        for i in range(len(nums)-1):
            if arr[i] in dup_list:
                return f"Duplicate element: {arr[i]}"
            dup_list.append(arr[i])
        return "No duplicates"

arr = [1,2,3,4,4,5]
sol = Solution()
print(sol.cont_dup(arr))        
"""

#Two Sums
"""
class Solution:
    def two_sums(self,nums,target):
        for i in nums:
            second = target - i
            if second in nums:
                return i, second
        return "No solution"
arr = [1,3,4,5,6]
sol = Solution()
print(sol.two_sums(arr,8))        
"""

#Best time to Buy and Sell stock
"""
class Solution:
    def maxprofit(self,prices:list[int]):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
    
prices = [1,2,5,6,78,2,1,0]
sol = Solution()
print(sol.maxprofit(prices))
"""

#Merge Two sorted arrays
"""
class Solution:
    def two_arr_merge(self,num1,num2):
        new_arr = []
        for i in num1:
            new_arr.append(i)
        for j in num2:
            if j in new_arr:
                pass
            else:
                new_arr.append(j)
        return new_arr

arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]
sol = Solution()
print(sol.two_arr_merge(arr1,arr2))
"""

#Remove duplicates from Sorted array
"""
arr = [1,2,2,3,4,5,6,7,8]
class Solution:
    def dup_rem(self,nums):
        check = []
        for i in arr:
            if i in check:
                arr.pop(i)
            else:
                check.append(i)
        print(arr)
sol = Solution()
sol.dup_rem(arr)            
"""

#Intersection of Two Arrays...
"""
arr1 = [1,2,3,4,5,6]
arr2 = [4,5,6,7,8,9]
class Solution:
    def intersec_arr(self,num1,num2):
        inter = []
        for i in arr1:
            for j in arr2:
                if i==j:
                    inter.append(i)
        print(inter)
sol = Solution()
sol.intersec_arr(arr1,arr2)
"""

#Majority Element
"""
arr = [1,2,3,3,4,4,4,5,6]
class Solution:
    def maj_ele(self, arr):
        max_count = 0
        element = None
        for i in arr:
            count = 0
            for j in arr:
                if i == j:
                    count += 1
            if count > max_count:
                max_count = count
                element = i
        return element
sol = Solution()
print(sol.maj_ele(arr))
"""

#Product Of Array execept self...
"""
arr = [1,2,3,4]
class Solution:
    def prod_ex_self(self,arr):
        left = [1] * len(arr)
        for i in range(1,len(arr)):
            left[i] = left[i-1] * arr[i-1]
        right = [1] * len(arr)
        for i in range(len(arr) - 2, -1, -1):
            right[i] = right[i + 1] * arr[i + 1]    
        answer = [left[i] * right[i] for i in range(len(arr))]
        print(answer)
sol = Solution()
sol.prod_ex_self(arr)
"""

#Maximum Subarray
"""
arr = [1,2,3,-4,5,-6,7,-9]
class Solution:
    def max_subarr(self,arr):
        count = 0
        max = 0
        new_sub = []
        for i in arr:
            count += i
            if count > max:
                max = count
                new_sub.append(i)
        print(new_sub)
sol = Solution()
sol.max_subarr(arr)
"""