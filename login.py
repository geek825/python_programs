class Login:
    def __int__(self,username,pasword):
        self.username = username
        self.password =password
    def login_details(self):
        try: 
            self.username = input("Enter the username :")
            self.password = input("Enter the password :")
        except ValueError:
            print("Please enter a valid username")
            
        if self.username== "yash" and self.password == "12345":
            print("login successful")
            
        else:
            print("Please check your usrname and password")
        
    def __str__(self):
        return f"username: {self.username}, pasword: {self.password}"
    
login1=Login()
print(login1.login_details())