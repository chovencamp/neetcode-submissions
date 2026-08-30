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

if "d" in your_dict:
  print("True")
else:
  print("False")

your_dict["a"] = 4
print(your_dict)
