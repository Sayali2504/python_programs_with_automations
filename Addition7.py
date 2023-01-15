print("Application to demonstrate industrial programming") #1

def Addition(Value1, Value2): #5
    Ans = Value1 + Value2
    return Ans #7

def main():  
    print("Enter First Number : ") #3
    no1 = int(input())

    print("Enter Second Number : ") #4
    no2 = int(input())

    sum=Addition(no1,no2) #5
    print("Addition is : ",sum) #8

if __name__ == "__main__":  #starter
    main()  #2