class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,new_deposit):
        print(f"balance changed from {self.balance} to {self.balance + new_deposit}")
        self.balance += new_deposit

    def withdraw(self,new_withdraw):
        print(f"balance changed from {self.balance} to {self.balance - new_withdraw}")
        self.balance -= new_withdraw

    def check_balance(self):
        print(f"{self.owner} have {self.balance}")

    def info(self):
        print(self.owner,self.balance)

yuval = BankAccount("yuval",200)
amit =  BankAccount("amit",150)
tal = BankAccount("tal",100)
shachar = BankAccount("shachar",0)


accounts = {
    "yuval": yuval,
    "amit": amit,
    "tal": tal,
    "shachar": shachar
}

while True:
    menu = int(input(
    "----------------------\n"
    "1 - deposit\n"
    "2 - withdraw\n"
    "3 - check_balance\n"
    "4 - info\n"
    "choose option(1/2/3):"))

    if menu == 1:
        choose = input("enter account name")
        amount = int(input("how much"))
        if choose in accounts:
            user = accounts[choose]
            user.deposit(amount)
            print("the user",user.owner,"have",user.balance)
    if menu == 2:
        choose = input("enter account name")
        amount = int(input("how much"))
        if choose in accounts:
            user = accounts[choose]
            user.withdraw(amount)
            print("the user",user.owner,"have",user.balance)
    
    if menu == 3:
        choose = input("enter account name")
        if choose in accounts:
            user = accounts[choose]
            print("the user",user.owner,"have",user.balance)

    if menu == 4:
        for choose in accounts:
            user = accounts[choose]
            user.info()