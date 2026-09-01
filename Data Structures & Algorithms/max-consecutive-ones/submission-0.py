class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Brute Force Method 
        result = 0 

        #loop through the list 
        for i in range(len(nums)):
            #set counter to reset to 0 on each iteration of the outer loop 
            counter = 0 
            #loop to check the streak 
            for j in range(i,len(nums)):
                #check if the postion of i is 0 if so break and go to outer loop for the next counter reset 
                if nums[j] == 0:
                    break
                #update the counter 
                counter += 1
            result = max(result, counter)
        return result
            

        