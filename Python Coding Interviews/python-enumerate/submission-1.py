from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    #loop using enumerate 
    for index, value in enumerate(nums):
        #if our list hits seven then return its index 
        if value == 7:
            return index
    #if there is no 7 in the list the the loop will be done and return -1 
    return -1 


def get_dist_between_sevens(nums: List[int]) -> int:
    #set the first index of seven to -1 in case in case we dont see a 7 at all 
    first_seven_index = -1
    #user a enumerate to loop over the list so we can get the index and value 
    for index,value in enumerate(nums):
        #if the value is 7 and the first seven has not been seen update it to the current index 
        if value == 7: 
            if first_seven_index == -1:
                first_seven_index = index
            #if the value is seven and we have already seen a 7 get the distance of it     
            else:
                return index - first_seven_index


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
