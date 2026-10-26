class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        num = []
        total = 0

        

        for i in nums:
            total = total + i
            num.append(total)
        return num

      
        