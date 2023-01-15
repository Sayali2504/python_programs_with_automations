print("Application to demonstrate industrial programming") #1

import MarvellousModule

def main():  
    print("__name__ from main is : ",__name__)
    print("Enter First Number : ") 
    no1 = int(input())

    print("Enter Second Number : ") 
    no2 = int(input())

    sum = MarvellousModule.Addition(no1,no2) 
    print("Addition is : ",sum) 

if __name__ == "__main__": 
    main()  