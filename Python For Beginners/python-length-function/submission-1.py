''' This program takes the two strings and finds which one is longer and 
returns that. If they are equal in length it will return the first word 
'''
def get_longer_word(word1: str, word2: str) -> str:
    if len(word1) > len(word2):
        return word1
    elif len(word2) > len(word1):
        return word2
    elif len(word2) == len(word1):
        return word1



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
