class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing = []

        minimum = min(nums)
        maximum = max(nums)

        for i in range(minimum, maximum + 1):
            nums_set = set(nums)
            if i not in nums_set:
                missing.append(i)

        return missing

