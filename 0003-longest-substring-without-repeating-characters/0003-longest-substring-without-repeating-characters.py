class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pack = set()
        left = 0
        long_char = 0
        current = 0
        for right in range(len(s)):
            while s[right] in pack :
                pack.remove(s[left])
                left += 1
            pack.add(s[right])
            current = right - left + 1
            long_char = max(long_char , current)
        return long_char  
                  