from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    #create new array that we will return 
    output = []
    #loop over the outer list
    for arr in nested_arr:
        #make a variable for the max of the array 
        max_in_arr = 0
        #loop on the inner list 
        for num in arr:
            #store the max array or the max number 
            max_in_arr = max(max_in_arr, num)
        #append the max into the list were returning 
        output.append(max_in_arr)
    #return the list 
    return output 



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
