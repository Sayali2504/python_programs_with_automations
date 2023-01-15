def main():
    
    Arr = list() #create empty list in python ->best way
    #Arr =[]
    print("Enter how many elements you want to store ? "
    )
    size = int(input())

    print("Please enter the values")

    for i in range(0,size):
        no = int(input())
        Arr.append(no) 
      #  Arr.insert(i,no) i=0,1,2,3,4... no = value enter by user

    print(Arr)    

if __name__ == "__main__":
    main()