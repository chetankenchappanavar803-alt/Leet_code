class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = str(x)
        rev = nums[::-1]
        if rev == nums :
            return True
        else : 
            return False
                