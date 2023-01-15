from functools import reduce


def main():
    print("Enter Number of Elements you want to enter : ")
    iSize = int(input())

    Data_Input = []
    print("Please enter the data ")

    for iCnt  in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is :", Data_Input)    

    Data_Filter = list(filter(lambda No :(No % 2 == 0) ,Data_Input))
    print("Data after FILTER:",Data_Filter)

    Data_Map = list(map(lambda No:No * 2,Data_Filter))
    print("Data after MAP is :",Data_Map)

    Data_Reduce = reduce(lambda A,B: A+B ,Data_Map)
    print("Data after REDUCE is :",Data_Reduce)

    # ans1 = reduce(lambda A,B: A+B ,Data_Map(list(map(lambda No:No * 2,Data_Filter))(list(filter(lambda No :(No % 2 == 0) ,Data_Input)))))
    # print(ans1)

if __name__ == "__main__":
    main()    