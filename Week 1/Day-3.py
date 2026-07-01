#Reverse a string
"""
class Solution:
    def rev_string(self, word):
        word = list(word)
        left, right = 0, len(word)-1
        while left < right:
            word[left], word[right] = word[right],word[left]
            left += 1
            right -= 1
        print("".join(word))
string = "World"
sol = Solution()
sol.rev_string(string)
"""

#Check Palindrome
"""
class Solution:
    def palindrome(self, word):
        word = list(word)
        new = word.copy()
        left, right = 0, len(new)-1
        while left < right:
            new[left], new[right] = new[right], new[left]
            left += 1
            right -= 1
        if new == word:
            return True
        else:
            return False
sol = Solution()
print(sol.palindrome("mad0m"))
"""

#Count vowels
"""
class Solution:
    def count_vol(self, string):
        vowels = ['a','e','i','o','u']
        count = 0
        for i in string:
            if i in vowels:
                count += 1
        print(count)
sol = Solution()
sol.count_vol("Axit")
"""

#Count Words
"""
class Solution:
    def count_word(self, words):
        count = 0
        in_word = False     
        for i in words:
            if i != " " and not in_word:
                count += 1
                in_word = True
            elif i == " ":
                in_word = False
        print(count)            
sol = Solution()
sol.count_word("I am Axit Patel ")
"""

#Remove Spaces
"""
class Solution:
    def rem_space(self, words):
        result = ""
        for i in words:
            if i == " ":
                continue
            result += i
        print(result)
sol = Solution()
sol.rem_space("Hello World")
"""

#Check Anagrams
"""
class Solution:
    def check_anagram(self, word1, word2):
        for i in word1:
            for j in word2:
                if i in word2:
                    if j in word1:
                        continue
                    else:
                        return False
                else:
                    return False
        return True
sol = Solution()
print(sol.check_anagram("listend","silent"))
"""

#First Non-Repeating Character
"""
class Solution:
    def non_rep(self, word):
        freq = {}
        for chars in word:
            freq[chars] = freq.get(chars, 0) + 1
        for i, chars in enumerate(word):
            if freq[chars] == 1:
                print("The First unique element is : ",word[i], "at index: ",i)
                return
        print("No Unique element Found")
sol = Solution()
sol.non_rep("HellloWORLDH")
"""

#Longest Common Prefix
"""
class Solution:
    def longest_common_prefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]        
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
sol = Solution()
words = ["Flowers","Flight","Fly"]
print(sol.longest_common_prefix(words))
"""

#Valid Parentheses
"""
class Solution:
    def valid_parentheses(self, word):
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        for chars in word:
            if chars in "({[":
                stack.append(chars)
            else:
                if not stack:
                    return False
                if stack.pop() != pairs[chars]:
                    return False
        return len(stack) == 0        
sol = Solution()
print(sol.valid_parentheses("({})"))
"""

#String Compression
"""
class Solution:
    def string_compression(self, string):
        count = 0
        current = string[0]
        new = ""
        for i in string[1:]:
            if i == current:
                count += 1
            else:
                new += current + str(count)
                current = i
                count = 1
        new += current + str(count)
        return new
sol = Solution()
print(sol.string_compression("aaaabbbbbbccccccc"))
"""