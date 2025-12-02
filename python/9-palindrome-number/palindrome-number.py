class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        # Numbers ending with 0 are not palindrome unless the number is 0
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0
        original = x

        # Reverse only half of the number
        while original > reversed_half:
            reversed_half = reversed_half * 10 + original % 10
            original //= 10

        # If digits count is even -> original should equal reversed_half
        # If digits count is odd  -> original should equal reversed_half // 10
        return original == reversed_half or original == reversed_half // 10
