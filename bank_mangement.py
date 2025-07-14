class BankAccount:
    def __init__(self,account_number,account_name,account_balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.account_balance= account_balance
        self.trans=[]
        if account_number == "8":
            print("Please enter a valid accound number")
       
    def deposit(self,amount):
        self.account_balance += amount
        self.trans.append(f"Deposited {amount} to {self.account_name}")
        print(f"Deposited {amount} to {self.account_name}") 
        print(f"New balance is {self.account_balance}") 
        
    def withdraw(self,amount):
        self.account_balance -= amount
        self.trans.append(f"Withdrawn {amount} {self.account_name}")
        print(f"Withdraw {amount} from {self.account_name}") 
        print(f"New balance is {self.account_balance}")
        
    def display_balance(self):
        print(f"Account number: {self.account_number}")
        print(f"Account name: {self.account_name}")
        print(f"Account balance: {self.account_balance}")
    def mini_statement(self,user_input):
        self.user_input = user_input
        if  user_input == "yes":
            for trans in self.trans:
                print(trans)
            print(f"account balance is {self.account_balance}")
            print(f"account number is {self.account_number}")
        
        elif user_input == "no":
            print("Thank you for using yash bank")
            
        else:
            print("Please enter a valid input")
         
            print(f"Account balance: {self.account_balance}")    
    def transfer(self,amount,other_account): 
        self.account_balance -= amount
        other_account.account_balance += amount
        print(f"Transferred {amount} from {self.account_name} to {other_account.account_name}")
    
            
    def __str__(self):
        return f"Account number: {self.account_number}, Account name: {self.account_name}, Account balance: {self.account_balance}" 
    
bank_account1 = BankAccount(input("Enter the account number : "),input("Enter the account name : "),1000)
bank_account1.deposit(int(input("Enter the amount to deposit :")))
bank_account1.withdraw(int(input("Enter the amount to withdraw")))
bank_account1.mini_statement(input("Do you want to see the mini statement? yes/no :"))
bank_account1.display_balance()
print(bank_account1)



