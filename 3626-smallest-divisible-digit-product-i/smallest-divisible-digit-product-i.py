class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
        # Calculate digit product
            curr = n
            prod = 1
            while curr > 0:
                prod *= curr % 10
                curr //= 10
            
        # Check if divisible by t
            if prod % t == 0:
                return n
        
        # Move to next number
            n += 1
    
