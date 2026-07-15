def remove_fourth_character(word: str) -> str:
    before_fourth_removed = word[:3] #this will cut everything after 3 givein us the first three of the string 
    after_fourth_removed = word[4:]
    return before_fourth_removed + after_fourth_removed 



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
