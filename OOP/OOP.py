'''
Accept 2 number and perform add and sub of it

OOP thinking 
-WHat do to (ky kraychay)? -> Behaviours (Functions)
ans = add and sub 
-Which things needed to do the same ?(te krayla ky lagnare ahe ) -> Charactiristics(Data)
ans = 2 number

Class = Charactiristics + Behavious 
Class =      Data       + Functions 
this = self '''

class Arithmatic:
    def __init__(self ,A,B): #compulsary mothod ,constructor is mandatory
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1 + self.No2 

    def Sub(self):
        return self.No1 - self.No2        


def main():
    print("Enter first number")
    value1 = int(input()) 

    print("Enter second number")
    value2 = int(input()) 

    obj = Arithmatic(value1,value2)

    Ans = obj.Add()
    print("Addition is :",Ans)

    Ans = obj.Sub()
    print("Sub is :",Ans)

if __name__ == "__main__":
    main()    