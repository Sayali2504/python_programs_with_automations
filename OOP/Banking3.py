'''
Instance variable : Name ,Amount , Address, AccountNo
Instance Method : CreateAccount(),DisplayAccountInfo(),Deposite(),Withdraw()
Class variable : Bank_Name , ROI_On_FD // can access without creating object
Class Method : DisplayBankInformation()
Static Method : DisplayKYCInfo()

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

        print("--------------Your account information is as below ----------------- ")
        print("Name of account holder : ",self.Name)
        print("Account Number  of account holder : ",self.AccountNo)
        print("Address of account holder : ",self.Address)
        print("Current amount in account : ",self.Amount)

    @classmethod #decorator to indicate it's class method
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposite is : ",cls.ROI_On_FD)

    @staticmethod   #decorator to indicate it's static method
    def DisplayKYCInfo():
        print("PLease consider below KYC information")
        print("According to the rules of Goverment of India you have to submit below documents")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of Aadhar card")
        print("3 : Photo of PAN card")

    def Deposite(self,value):
        self.Amount = self.Amount + value   

    def Withdraw(self,value):
        self.Amount = self.Amount - value         
       
def main():

    Bank_Account.DisplayKYCInfo()
    Bank_Account.DisplayBankInformation()

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the first account ")
    User1.CreateAccount()
    print("Creating the second account ")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposite(500)
    User2.Deposite(1200)

    print("Amount of {} after deposit us {} :",format(User1.Name,User1.Amount))
    print("Amount of {} after deposit us {} :",format(User2.Name,User2.Amount))
    
    User1.Withdraw(100)
    User2.Withdraw(100)

    print("Amount of {} after Withdraw us {} :",format(User1.Name,User1.Amount))
    print("Amount of {} after Withdraw us {} :",format(User2.Name,User2.Amount))




if __name__ == "__main__":
    main()    
