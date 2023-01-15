
def Display(No):
    if(No > 0):
        print(No)
        No = No -1
        Display(No) #Recursive call #tail recursion - at end of function

Display(4)

        