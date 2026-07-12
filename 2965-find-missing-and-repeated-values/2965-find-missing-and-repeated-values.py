class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                nums.append(grid[i][j])
        N = len(nums)
        expected_sum = (N * (N+1)) // 2
        actual_sum = sum(nums)
        set_sum = sum(set(nums))
        ele = expected_sum - set_sum
        dub = actual_sum - set_sum
        return [dub , ele]       