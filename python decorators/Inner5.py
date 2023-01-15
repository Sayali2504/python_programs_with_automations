
def Substration(No1 , No2):#200  #already defined we cannot edit this function , to Pass greater number to substration we used decorator . 
    Ans = 0
    Ans = No1 - No2 
    return Ans

def Decorated_Function(Function_Name):  #Function+Name = 200          #decorator
    def Inner (A,B): #300
        if(A < B):
            A,B = B,A #Swapping of number 
        output = Function_Name(A,B) #  200(12,8) Substration(12,8)
        return output # 4 
    return Inner #return 300


def main(): #100
    Value1 = int(input("Enter First Number :")) # Val1 = 8
    Value2 = int(input("Enter Secnod Number: ")) # Val2 = 12 


    New_Function = Decorated_Function(Substration) #Decorate_Function(200)
    Ret = New_Function(Value1,Value2)  # ret =300(8,12)
    print("Substration is :",Ret)

if __name__ == "__main__":
    main() #call 100()


