#Search in a sorted array (Rotated)
"""
def search_arr(arr,ele):
    left,right = 0, len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid]==ele:
            return mid        
        if arr[left] <= arr[mid]:
            if arr[left] <= ele < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] <= ele < arr[right]:
                left = mid + 1
            else: 
                right = mid - 1
    return -1 
print(search_arr([2,3,4,5,6,0],1))
"""

#The issue with normal binary search
"""
def search_arr(arr,ele):
    left,right = 0, len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid]==ele:
            return mid
        elif arr[mid] > ele:
            left = mid + 1
        else:
            right = mid - 1
print(search_arr([6,7,8,9,0,1,2,3,4,5],4))
"""

#Floor and Ceil 
"""
def floor_and_ceil(arr,ele):
    left,right = 0, len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == ele:
            return arr[mid-1], arr[mid+1]
        elif arr[mid] < ele:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(floor_and_ceil([1,2,3,4,5,6,7,8],4))        
"""

#Aggressive Cows
"""
def can_place(stalls, cows, distance):
    count = 1
    last = stalls[0]
    for stall in stalls[1:]:
        if stall - last >= distance:
            count += 1
            last = stall
        if count == cows:
            return True
    return False
def aggressive_cows(stalls, cows):
    stalls.sort()
    left = 1
    right = len(stalls)-1
    ans = 0
    while left <= right:
        mid = (left+right)//2
        if can_place(stalls,cows,mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
print(aggressive_cows([1,2,3,4,5,6,7,8],3))
"""

#Split arr largest sum
"""
def arr_largest_sum(arr,k):
    left,right = max(arr),sum(arr)
    while left<right:
        mid = (left+right)//2
        current_sum = 0
        k_ = 1
        for i in arr:
            if current_sum + i > mid:
                k_ += 1
                current_sum = 0
            current_sum += i
        if k_ <= k:
            right = mid
        else: 
            left = mid + 1
    return left
print(arr_largest_sum([7,2,15,10,19],2))
"""