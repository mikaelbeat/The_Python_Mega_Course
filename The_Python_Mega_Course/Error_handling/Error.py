

def calculate(value1, value2):
    try:
        return value1 + value2
    except:
        return "Both values must be integer"
    

print(calculate(1, 5))