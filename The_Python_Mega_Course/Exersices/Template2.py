
numbers = [1, 2, 3]

def writer(data):
    data_file = "numbers.txt"
    file = open(data_file, "a+")
    for value in data:     
        file.write(str(value) + "\n")
    file.close() 

writer(numbers)


print("\n********************\n")


temperatures = [10, -20, -289, 100]

def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f
for t in temperatures:
    data = (c_to_f(t))
    with open("data2.txt", "a+") as file:
        if type(data) == str:
            ""
        else:
            file.write(str(data) + "\n")
    
    
c_to_f(1)