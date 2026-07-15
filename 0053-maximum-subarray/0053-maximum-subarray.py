class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        max_ = - 10**18
        for i in range(0, len(nums)):
            sum_ += nums[i]
            max_ = max(max_,sum_)
            if sum_ < 0  :
                sum_ = 0
        return max_
        