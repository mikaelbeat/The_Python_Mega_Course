

data_file = "data.txt"

# with open(data_file, "r") as file:
#     print(file.read())
# 
# 
# 
# 
# file = open("Data.txt", 'r')
# print(file.read())
# file.close()




data = open(data_file, "r")
content = data.read()
data.close()
content = content.splitlines()
for value in content:
    print(len(value))
    
    
    
2 - 50
