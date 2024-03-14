#parameterized and non parameterized constructor
#this will be used in the web automation

class VWLoginpage:
    email=None
    password=None
    def __init__(self,email,password):
        self.email=email
        self.password=password

    def login_confirm(self):
        if self.password == "Pass123":
            print("Login Successfull")
        else:
            print("Login Incorrect")
subham =VWLoginpage("subahm@routineai.com","Pass")
subham.login_confirm()

aaru=VWLoginpage("aaru@gmai.com","Pass123")
aaru.login_confirm()