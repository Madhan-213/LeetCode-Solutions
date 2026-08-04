class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing = []

        minimum = min(nums)
        maximum = max(nums)

        for i in range(minimum, maximum + 1):
            if i not in nums:
                missing.append(i)

        return missing

