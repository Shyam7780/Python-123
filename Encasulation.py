#Encapsulation use

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance  #private veriable
        
    #geter function
    @property
    def getBalance(self):
        return self.__balance
    def Deposit(self,deposit):
        self.balance+=deposit
    def Withdraw(self,W_amount):
        if W_amount>self.__balance:
            print("Erorr")
        else:
            print(f"Withdraw Amount ={W_amount} \n Current Balance ={B1.getBalance}")
            self.__balance-=W_amount
            
B1=BankAccount("Shyam",1000000)

print(B1.getBalance)
B1.Withdraw(2000)
print(B1.getBalance)
print(B1.__balance)
