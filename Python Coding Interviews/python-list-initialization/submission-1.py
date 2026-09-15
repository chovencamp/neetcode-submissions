from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    #make sure that the list is the size that is being passed and set to 0 aside from where the index is that we assign the value. 
    list = [0] * size 
    list[index] = value
    return list



# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
