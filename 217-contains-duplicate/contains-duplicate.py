class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        nums.sort()

        left = 0
        right = len(nums) - 1


        twice = False
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                twice = True
                break
        return twice