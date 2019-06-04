
data1 = 5
data2 = "Text"
data3 = "6"

print("\n***** Data is int *****\n")
print(type(data1))

print("\n***** Data is str *****\n")
print(type(data2))


print("\n***** Check data type *****\n")
if isinstance(data3, str):
    print("Data is string")
elif isinstance(data3, int):
    print("Data is interger")