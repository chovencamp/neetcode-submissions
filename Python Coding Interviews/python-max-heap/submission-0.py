import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    maxHeap = [] 

    for num in nums: 
        #push the - number into the heap to create a min heap 
        heapq.heappush(maxHeap, -num)
    
    #loop while there is something in the heap 
    result = []
    while maxHeap: 
        result.append(-heapq.heappop(maxHeap))
        

    return result 

    







# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
