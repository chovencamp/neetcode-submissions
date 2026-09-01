class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0 
        count = 0 

        #check each element in the array to see if its a 0 or 1 
        for num in nums:
            #check if the value is 0. If it is then reset the count and store the max of the result and count 
            if num == 0: 
                result = max(result,count)
                count = 0
            #if the number is 1 update the counter 
            else:
                count += 1
        return max(result,count)

            

        