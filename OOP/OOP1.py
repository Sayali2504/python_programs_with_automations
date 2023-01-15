
class Arithmetic: #OOP
    def __init__(self,A,B): #special method self- is a keyword (related to this keyword)(like constructor - constructor call automatically call after allocating memory for object)
        print("Inside init method")
        self.No1 = A #instance variable 
        self.No2 = B #instance variable 

    def Addition(self): #if first parameter is 'self' then it is instance method
        Ans = self.No1 + self.No2 
        return Ans 

    def Substration(self):
        Ans = self.No1 - self.No2
        return Ans     

def main(): #procedural
    print("Inside main method")

    obj = Arithmetic(11,10) #object of class 
    Output = obj.Addition()
    print("Addition is :", Output)
    Output = obj.Substration()
    print("Substration is :", Output)

  
    
if __name__ == "__main__": #scripting
    print("Inside started ")
    main()    