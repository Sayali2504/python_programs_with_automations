
def Fact(No): 
    if (No <= 1):
        return 1
    else:
        return (No * Fact(No - 1)) 

Value = Fact(5); 
print("Result is  : ",Value)