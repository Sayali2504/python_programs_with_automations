def Add1(No1,No2):
    print("Value of no: ",No1)
    print("Value of no: ",No2)

    return No1+No2

def Sub1(No1,No2):
    print("Value of no: ",No1)
    print("Value of no: ",No2)

    return No1-No2    

def main():
    Ans = Add1(10,11) #positional argument -send parameters in line , can use when know the parameters
    print("sum is : ",Ans)

    Ans = Sub1(No2=10,No1=11) #keyword argument - send parameters by using name, can use when dont know the sequence 
    print("sub is : ",Ans)


if __name__ == "__main__":
    main()    