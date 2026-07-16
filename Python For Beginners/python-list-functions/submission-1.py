from typing import List # this is used to add type hints for List type

# def get_sum(nums: List[int]) -> int:
#     return sum(nums)

# def get_min(nums: List[int]) -> int:
#     return min(nums)

# def get_max(nums: List[int]) -> int:
#     return max(nums)

'''Harder Challenge'''

def get_sum(nums: List[int]) -> int: 
    #loop through the list take whatever the element is and add it so a sum 
    sum = 0 
    for i in nums: #loop over the list 
        sum += i
    return sum 
    
def get_min(nums: List[int]) -> int:
    #create a min value 
    min = nums[0]
    #loop through the list 
    for num in nums: 
        if num < min:
            min = num
    return min

def get_max(nums: List[int]) -> int:
    #set a max value to first index in the list 
    max = nums[0]
    #loop the list 
    for num in nums: 
        if num > max:
            max = num 
    return max 

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
