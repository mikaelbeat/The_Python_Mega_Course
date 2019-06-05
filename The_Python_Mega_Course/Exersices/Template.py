


def string_length(value):
    if type(value) != str:
        return f"Value {value} is not a string!"
    else:
        return len(value)
    
    
print(string_length(7))



mylist = [1, 2, 3, 4, 5]


for value in mylist:
    if value > 2:
        print(value)
    