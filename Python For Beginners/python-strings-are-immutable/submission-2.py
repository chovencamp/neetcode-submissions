def remove_fourth_character(word: str) -> str:
    before_fourth_removed = word[:3] #this will cut everything after 3 givein us the first three of the string 
    after_fourth_removed = word[4:] #this will start at 4 which means it will slice 4 and below off 
    return before_fourth_removed + after_fourth_removed #Concatenating this will allow for us to have the string without the 4th index from the original string 



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
