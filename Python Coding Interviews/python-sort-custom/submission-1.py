from typing import List

def sort_len(words: List[str]) -> List[str]:
    #return the lenth of our list 
    return len(words)

def abs_sort(words: List[str]) -> List[str]:
    #return the abs value of the list 
    return abs(words)

def sort_words(words: List[str]) -> List[str]:
    #do a sort custom to get the length and put the list in order by descending so the longest word first
    words.sort(key = sort_len, reverse = True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    #do a custom sort to get absolute value of the sort and keep reverse true for ascending order 
    numbers.sort(key = abs_sort, reverse = False)
    return numbers




# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
