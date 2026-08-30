your_dict = { 
  "a": 10, 
  "apple": 12,
  "bat": 7
}

#prints the whole dict
print(your_dict)
#print the value of a 
print(your_dict["a"])
#print true or flase based on if d is in the dicitonary 

#check if d is in our dict if not print false if so print true 
if "d" in your_dict:
  print("True")
else:
  print("False")

#set the key of "a" to be assinged a value of 4 
your_dict["a"] = 4
#print out the full dict 
print(your_dict)
