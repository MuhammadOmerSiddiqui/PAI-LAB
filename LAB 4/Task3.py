class Account:
    def __init__(self):
        self.__account_no = ""
        self.__account_bal = 0.0
        self.__security_code = 0 
    def set_data(self,account_no,account_bal,security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code
    def print_data(self):
        print(f"The account number is {self.__account_no}")
        print(f"The account balance is {self.__account_bal}")
        print(f"The security code is {self.__security_code}")

account = Account()
account.set_data("1234",20000,4567)
account.print_data()