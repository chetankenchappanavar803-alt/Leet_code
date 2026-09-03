class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = nums.count(0)
        for i in range(zeros) :
            nums.remove(0)
            nums.append(0)
        