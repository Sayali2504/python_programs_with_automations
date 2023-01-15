
class Numbers: 
    def __init__(self): 
        self.size = 0
        self.Arr=list()

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


def main(): 
    obj = Numbers()
    obj.Accept()
    obj.Display()
    

if __name__ == "__main__": 
    main()    