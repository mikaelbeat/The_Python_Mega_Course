


def string_length(value):
    if type(value) != str:
        return f"Value {value} is not a string!"
    else:
        return len(value)
       
print(string_length("2019"))
print(string_length(2019))


print("\n******************************\n")


mylist = [1, 2, 3, 4, 5]

for value in mylist:
    if value > 2:
        print(value)
        
        
print("\n******************************\n")

temperatures = [10, -20, 100]

def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return f"Celcius {celsius} is in fahrenheit {fahrenheit}"

print(cel_to_fahr(27))  


print("\n******************************\n")


def cel_to_fahr2(data):
    for value in data:
        fahrenheit = value * 9/5 + 32
        print(f"Celcius {value} is in fahrenheit {fahrenheit}")
    return ""

print(cel_to_fahr2(temperatures))


print("\n******************************\n")


def cel_to_fahr3(data):
    for value in data:
        fahrenheit = value * 9/5 + 32
        result = f"Celcius {value} is in fahrenheit {fahrenheit}"
        print(result)
        data_file = open("temperatures_data.txt", "a")
        data_file.write(result + "\n")
        data_file.close()
    return ""

print(cel_to_fahr3(temperatures))








