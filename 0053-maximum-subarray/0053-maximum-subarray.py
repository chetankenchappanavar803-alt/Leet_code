class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        max_ = - 10**8
        for i in range(len(nums)):
            sum_ += nums[i]
            max_ = max(max_, sum_)
            if sum_ < 0 :
                sum_ = 0
        return max_
            
        