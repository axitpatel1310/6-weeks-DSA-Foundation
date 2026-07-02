#Frequency Counter
"""
class Solution:
    def freq_count(self, string):
        freq = {}
        for i in string:
            freq[i] = freq.get(i,0)+1
        return freq
sol = Solution()
print(sol.freq_count("aaabbbbcccc"))
"""
#Find Duplicate Numbers
"""
class Solution:
    def duplicate_num(self, list):
        dup_freq = {}
        for i in list:
            dup_freq[i] = dup_freq.get(i, 0)+1
        return {k: v for k, v in dup_freq.items() if v > 1}
sol = Solution()
print(sol.duplicate_num([1,2,3,4,5,6,7,6,7,6,6]))
"""

#Isomorphic Strings
"""
class Solution:
    def isomorphic_string(self, string1,string2):
        map_s_to_t = {}
        map_t_to_s = {}
        for char_s, char_t in zip(string1,string2):
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t        
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s
        return True
sol = Solution()
print(sol.isomorphic_string("aad","eeg"))
"""

#Happy Numbers
"""
class Solution:
    def happy_num(self, nums):
        new = []
        for i in nums:
            new.append(i ** 2)
        total = 0
        for j in new:
            total += j 
        print(f"{new} : {total}")   
sol = Solution()
sol.happy_num([1,2,3,4])
"""
