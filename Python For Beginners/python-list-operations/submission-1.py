def check_list_empty(my_list: list[str]) -> bool:
    if my_list: #if list is empty return true if not return false 
        return False 
    return True

def check_element_in_list(my_list, element) -> bool:
    if element in my_list:
        return True 
    else: 
        return False 

# do not modify below this line
print(check_list_empty([]))
print(check_list_empty([1, 2, 3]))

print(check_element_in_list([1, 2, 3], 1))
print(check_element_in_list([1, 2, 3], 4))

print(check_element_in_list(["Apple", "Banana", "Orange"], "Banana"))
print(check_element_in_list(["Apple", "Banana", "Orange"], "Grape"))
