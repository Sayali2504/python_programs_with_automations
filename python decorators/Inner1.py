#can write function within a function - Inner Function 

def Hello():
    print("Inside Demo")

    def Demo():
        print("Inside Hello")

    Demo()

Hello()
  
