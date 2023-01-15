def CheckEven(No):
    return (No % 2 == 0) #Will return true or false  

def Doubles(No):
    return No * 2

def Sum(A,B):
    return A+B 

def filterX(Help_Function,Data):
    Result = []
    for No in Data:
        if(Help_Function(No) == True):
            Result.append(No)

    return Result  

def mapX(Helper_Function,Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)

    return Result     

def reduceX(Helper_Function,Data):
    Ans = 0
    for No in Data:
        Ans = Helper_Function(Ans,No)

    return Ans      

def main():
    print("Enter Number of Elements you want to enter : ")
    iSize = int(input())

    Data_Input = []
    print("Please enter the data ")

    for iCnt  in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is :", Data_Input)    

    Data_Filter = filterX(CheckEven,Data_Input)
    print("Data after FILTER:",Data_Filter)

    

    Data_Map = mapX(Doubles,Data_Filter)
    print("Data after MAP is :",Data_Map)


    Data_Reduce = reduceX(Sum,Data_Map)
    print("Data after REDUCE is :",Data_Reduce)

if __name__ == "__main__":
    main()    