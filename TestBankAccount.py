from ClassBankAccount import BankAccount

myaccount = BankAccount(1000)

myaccount.Deposit(200)
myaccount.CheckBalance()

myaccount.Withdraw(2000)
myaccount.CheckBalance()

myaccount.Withdraw(-100)
myaccount.CheckBalance()

myaccount.Withdraw(100)
myaccount.CheckBalance()