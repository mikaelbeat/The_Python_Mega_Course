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
    
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
        
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        
        
checking = Checking("Balance.txt", 10)

checking.deposit(10)
checking.commit()       
print(checking.balance)
 
checking.transfer(550)
checking.commit()
print(checking.balance)