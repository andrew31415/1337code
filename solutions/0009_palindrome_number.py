"""https://leetcode.com/problems/palindrome-number/description/
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        orig = abs(x)
        reverse = 0

        while orig:
            reverse = reverse * 10 + orig % 10
            orig //= 10

        return reverse == x
