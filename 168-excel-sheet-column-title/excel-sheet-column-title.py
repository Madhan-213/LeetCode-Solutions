class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            reminder = columnNumber % 26
            result = chr(ord('A') + reminder) + result
            columnNumber //= 26
        return result