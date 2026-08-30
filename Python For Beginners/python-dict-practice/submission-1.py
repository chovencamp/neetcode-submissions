from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    #create a empty dict 
    char_count = {}
    for char in word:
        if char in char_count:
            #update the counter if its in dict aready
            char_count[char] +=1
        else:
            #this is where we store stuff in the dict that isnt there and assign the count as the value 
            char_count[char] = 1
    return char_count





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
