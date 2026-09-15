from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    #append the elements of arr2 to arr1 
    for value in arr2:
        #append the value were looping on to array1 
        arr1.append(value)
    #return the array 
    return arr1


def pop_n(arr: List[int], n: int) -> List[int]:
    #do a while loop that as long as our n is greater than so and the array is not empty pop n times 
    while n > 0 and len(arr) > 0:
        arr.pop()
        #update n so we can break the loop 
        n -= 1
    return arr 
    

def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    #check if the index is out of bounds if so than just append the element to the list 
    if index > 0 or index <= len(arr):
        arr.insert(index, element)
    else: 
        arr.append(element)

    return arr
  


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
