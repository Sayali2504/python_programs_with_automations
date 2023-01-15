
class Numbers: 
    def __init__(self): 
        self.size = 0
        self.Arr=list()
        self.Accept()

    def Accept(self):
        print("How many elements you want to store ?")  
        self.Size = int(input())
        Value = 0
        print("Enter the elements: ")
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)

   
    def Display(self):
        print("Elements from list are:")
        for i in range(0,self.Size):
            print(self.Arr[i])      

   
    def Summation(self):
        Sum = 0 #local variable
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]
        return Sum 

    def Average(self):
        Sum = 0 #local variable
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]
        return (Sum/self.Size)   

    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0,self.Size):
           if(self.Arr[i] > Max):
                Max = self.Arr[i]
        return Max   

    def Minimum(self):
        Min = self.Arr[0]
        for i in range(0,self.Size):
           if(self.Arr[i] <  Min):
                Min = self.Arr[i]
        return Min                          

    def __CheckPrime(self,No): #private method - not accessible outside class
        i = 0 
        Flag = True
        for i in range(2,int(No/2)+1):
            if(No % i == 0):
                Flag = False
                break
        return Flag 

    def DisplayFactors(self):
        for i in range(0,self.Size):
            if(self.__CheckPrime(self.Arr[i]) == True):
                print("{} is a prime number:".format(self.Arr[i]))



def main(): 
    obj = Numbers()
    #obj.Accept()
    obj.Display()

    Output = obj.Summation()
    print("Sum of all elements is:",Output)

    Output = obj.Average()
    print("AVerage of all elements is:",Output)

    Output = obj.Maximum()
    print("Max of all elements is:",Output)

    Output = obj.Minimum()
    print("Min of all elements is:",Output)

    Output = obj.DisplayFactors()
    # print("Factors are :",Output)
    

if __name__ == "__main__": 
    main()    