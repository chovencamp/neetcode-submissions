import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    #create a min heap 
    minHeap = [] 

    #loop over the list and negate the numbers into our heap which will give is the smallest number on top. 
    for num in nums:  
        heapq.heappush(minHeap, -num)
    
    
    #create a max heap that will be our reversed list 
    maxHeap = []
    while minHeap: 
        #take the min heap and negate again to get the max value and then append to the list so that it is reversed. 
        maxHeap.append(-heapq.heappop(minHeap))
        
    #return the reversed list. 
    return maxHeap

    
# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
