#Search a 2D Matrix
"""
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False    
    rows = len(matrix)
    col = len(matrix[0])
    left,right = 0, rows * col - 1
    while left <= right:
        mid = (left + right) // 2
        r = mid // col
        c = mid % col
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [10,32,34,56]
]
print(searchMatrix(matrix,34))
"""

#Find K Closest Element
"""
def findClosestElements(arr, k, x):
    n = len(arr)
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    l = left - 1
    r = left
    result = []
    while k > 0:
        if l < 0:
            result.append(arr[r])
            r += 1
        elif r >= n:
            result.append(arr[l])
            l -= 1
        elif abs(arr[l] - x) <= abs(arr[r] - x):
            result.append(arr[l])
            l -= 1
        else:
            result.append(arr[r])
            r += 1
        k -= 1
    return sorted(result)
arr = [1,2,3,4,5,6,7,8,9]
print(findClosestElements(arr,3,2))
"""

#Median of Two Sorted Arrays
"""
class Solution:
    def findMedianSortedArr(self,a,b):
        if len(a) > len(b):
            a,b = b,a
        m,n = len(a),len(b)
        left,right = 0,m
        while left <= right:
            i = (left + right) // 2
            j = (m+n+1)//2 - i            
            aleft = float("inf") if i == 0 else a[i-1]
            aright = float("inf") if i == m else a[i]
            bleft = float("-inf") if j == 0 else b[j-1]
            bright = float("inf") if j == n else b[j]
            if aleft <= bright and bleft <= aright:
                if (m+n)%2:
                    return max(aleft,bleft)
                return (max(aleft,bleft) + min(aright,bright)) / 2
            elif aleft > bright:
                right = i - 1
            else:
                left = i + 1
sol = Solution()
print(sol.findMedianSortedArr([1,2,3,4,5],[10,11,12,13,14]))
"""

#Aggressive Cows
