from typing import List


def sort_words(words: List[str]) -> List[str]:
    #use a lamda for the key so we dont have to make a seperate function for length 
    # pass the argument of word to the lamda and have its body take the length of that word 
    words.sort(key = lambda word: len(word), reverse = True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    #user a lambda function to get the absolute value of the number 
    numbers.sort(key = lambda number: abs(number), reverse = False)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
