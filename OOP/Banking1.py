'''
Instance variable : Name ,Amount , Address, AccountNo
Instance Method : CreateAccount(),DisplayAccountInfo()
Class variable : Bank_Name , ROI_On_FD // can access without creating object
Class Method : DisplayBankInformation()


'''


class Bank_Account:

    Bank_Name = "HDFC Bank PVT LTD"
    ROI_On_FD = 6.7

    def __init__(self): #constructor

        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0


    def CreateAccount(self):
        print("Enter your name :")
        self.Name = input()

        print("Enter your initial Amount :")
        self.Amount = int(input())

        print("Enter your Address :")
        self.Address = input()

        print("Enter your Account number :")
        self.AccountNo = int(input())  

    def DisplayAccountInfo(self):

        print("--------------Your account information is as below --------------------- ")
        print("Name of account holder : ",self.Name)
        print("Account Number  of account holder : ",self.AccountNo)
        print("Address of account holder : ",self.Address)
        print("Current amount in account : ",self.Amount)

    @classmethod #decorator to indicate it's class method
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposite is : ",cls.ROI_On_FD)


       
def main():

    print("Name of bank : ",Bank_Account.Bank_Name)
    print("Rate of intrest on Fixed deposit : ",Bank_Account.ROI_On_FD)

    Bank_Account.DisplayBankInformation()


    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the first account ")
    User1.CreateAccount()
    print("Creating the second account ")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ == "__main__":
    main()    
