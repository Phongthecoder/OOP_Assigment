class BankAccount():
    def __init__(self, initial_amount: 0.0):
        # Valid initial amount
        assert initial_amount >= 0, f"{initial_amount} is smaller than 0"
        self.__balance = initial_amount #private variable
    
    def CheckBalance(self):
        print(f"Balance: {self.__balance}")
        
    def Deposit(self, deposit_amount: float):
        if deposit_amount < 0:
            print(f"{deposit_amount} is smaller than 0")
        else:
            self.__balance = self.__balance + deposit_amount
            
    def Withdraw(self, withdraw_amount):
        if withdraw_amount < 0:
            print(f"{withdraw_amount} is smaller than 0")
        elif withdraw_amount > self.__balance:
            print(f"Not enough money to withdraw")
        else:
            self.__balance = self.__balance - withdraw_amount

