
def Display(No):
    Cnt = 0 
    if(No > 0):
        print("Hello")
        No = No - 1
        Display(No) #recursive function call 

Display(4) #function call 
        