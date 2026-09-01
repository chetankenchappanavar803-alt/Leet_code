class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = str(x)
        if nums[::-1] == nums :
            return True
        else : 
            return False
                