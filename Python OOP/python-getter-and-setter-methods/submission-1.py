class BankAccount:
    def __init__(self, balance: int):
        #make this attribute private 
        self.__balance = balance 
    
    # TODO: Add getter method for balance
    def get_balance(self):
        #return the balance 
        return self.__balance

    # TODO: Add setter method for balance
    def set_balance(self,new_balance):
        #make sure the balance is greater than or equal to 0 
        if new_balance >= 0:
            #set the attribute to the new balance 
            self.__balance = new_balance
        else: 
            print(f"Cannot set negative balance!")




# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
