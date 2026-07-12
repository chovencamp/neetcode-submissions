def add_one(n):
    n = n + 1
    print(n)   

n = 10

add_one(n)     # Output: 11

print(n)       #It is 10 because there is no return on add_one that will store any updated version. that plus one only exists in the scope of that function
