#Square root of element
"""
class Solution:
    def square_root(self, num):
        if num < 2:
            return num
        left, right = 1, num
        while left <= right:
            mid = (left + right)//2
            if mid * mid == num:
                return mid
            elif mid * mid < num:
                left = mid+1
            else:
                right = mid-1
        return right
sol = Solution()
print(sol.square_root(8))
"""

#Koko Eating Bananas
"""
class Solution:
    def koko_eating_banana(self,arr,h):
        left,right = 1, max(arr)
        while left < right:
            mid = (left + right) // 2
            hours = 0
            for a in arr:
                hours += (a + mid - 1) // mid
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left
sol = Solution()
print(sol.koko_eating_banana([1,10,10,20],10))
#if you have 10 hours to finish 41 banans how many per hour you'll eat
"""



#Capacity to Ship Packages within D days
"""
class Solution:
    def ship_pack(self,arr,d):
        left,right = max(arr), sum(arr)
        while left < right:
            mid = (left + right) // 2
            days = 1
            curr = 0
            for weight in arr:
                if curr + weight > mid:
                    days += 1
                    curr = 0
                curr += weight
            if days <= d:
                right = mid
            else:
                left = mid + 1
        return left
sol = Solution()
print(sol.ship_pack([1,2,3,4,5,6],50))
"""

#Minimum Days to Make M Bouquets
"""
class Solution:
    def make_bouquet(self, bloomDay,m,k):
        if m * k > len(bloomDay):
            return -1
        def canMake(day):
            bouquets = 0
            flowers =  0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else: 
                    flowers = 0
            return bouquets >= m
        left = min(bloomDay)        
        right = max(bloomDay)                
        while left <= right:
            mid = (left+right)//2
            if canMake(mid):
                right = mid-1
            else:
                left = mid + 1
        return left
sol = Solution()
print(sol.make_bouquet([1,20,33,4,35,9,12],3,2))
"""