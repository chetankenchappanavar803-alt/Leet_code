class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums1)-1,m-1,-1) :
            nums1.remove(nums1[i])
        for num in nums2 :
            nums1.append(num)
        return nums1.sort()            
                      

