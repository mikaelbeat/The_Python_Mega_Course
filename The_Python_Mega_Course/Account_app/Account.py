class Account:
    
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as file:
            self.balance = int(file.read())
            
    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))
            

account = Account("Balance.txt")
# print(account.balance)
# 
# account.withdraw(500)
# print(account.balance)
# 
# account.deposit(700)
# print(account.balance)
# 
# account.commit()



class Checking(Account):
    
    """This class generates checking account objects"""
    
    type = "checking"
    
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
        
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        
        
jack_checking = Checking("Jack.txt", 10)
jack_checking.deposit(10)
jack_checking.commit()       
print(jack_checking.balance)
print(jack_checking.type)
print(jack_checking.__doc__)

print("\n***************\n")

john_checking = Checking("John.txt", 10) 
john_checking.transfer(100)
john_checking.commit()
print(john_checking.balance)