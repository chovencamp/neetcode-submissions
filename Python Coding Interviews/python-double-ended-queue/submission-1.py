from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    rotatedQueue = deque(arr)
    #loop k times 
    for i in range(k):
        #pop first so it will pop k times and then append to the left. This simulates the list rotating. 
        rotatedQueue.appendleft(rotatedQueue.pop())
        #return the updated list
    return rotatedQueue



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
