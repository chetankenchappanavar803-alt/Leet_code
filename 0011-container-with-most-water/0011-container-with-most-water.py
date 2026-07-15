class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = []
        lp = 0 
        rp = len(height) - 1
        while lp < rp :
            width = rp - lp
            ht = min(height[lp],height[rp])
            ans = ht*width
            max_.append(ans)
            if height[rp] < height[lp] :
                rp -= 1
            else :
                lp += 1
        return max(max_)

        

        
        