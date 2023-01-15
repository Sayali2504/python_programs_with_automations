
def Display(No):
    if(No > 0):
        No = No - 1
        Display(No) #Recursive call #head recursion - not at end of function 
        print(No+1)

Display(4)

        