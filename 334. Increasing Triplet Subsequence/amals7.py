class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf') # positive infitiy 
        for n in nums:
            if n <= first:
                first = n
                print(first)
            elif n <= second :
                second = n
                print(second)
            elif n>second:
                return True
        return False
        