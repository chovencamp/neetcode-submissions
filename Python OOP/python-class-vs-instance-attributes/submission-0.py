class BankAccount: 
    #class attributes 
    total_accounts = 0 
    total_balance = 0 
    
    def __init__(self,name,balance) -> None:
        #instance attributes 
        self.__name = name
        self.__balance = balance 
        #class attribute update for each instance 
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

    @property 
    def name(self):
        return self.__name
    
    @property 
    def balance(self):
        return self.__balance

    @name.setter
    def name(self,new_name):
        self.__name = new_name 
    
    @balance.setter 
    def balance(self,new_balance):
        BankAccount.total_balance += new_balance - self.__balance
        self.__balance = new_balance 


alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 2000)

print(f"{alice_account.name}'s balance: ${alice_account.balance}")
print(f"{bob_account.name}'s balance: ${bob_account.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")