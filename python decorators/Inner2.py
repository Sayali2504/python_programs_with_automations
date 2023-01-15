#passing function as parameter to another function 

def Demo():
    print("Inside Demo")


def Fun():
    print("Inside Fun")

def Hello(FPTR):  #Nacked prototyping 
        print("Inside Hello")
        FPTR()

Hello(Demo)
Hello(Fun)
