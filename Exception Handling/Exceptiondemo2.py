
def main():

    try: #python is compiled becuse if you dont write complete syntax it will give error . Means no pyc file is generated erro is given before. 
        print("Enter first number")
        No1 = int(input())

        print("Enter second number")
        No2 = int(input())

        
        Ans = No1 / No2
        print("Division is:",Ans)

    # except ZeroDivisionError:
    #     print("Inside zero division error")     

    # except ValueError:
    #     print("Inside value error")  


     #MSD Dhoni handle all exception
    except Exception as e:
        print(str(e))    

    finally : # 1.if file is open and program is stop due to exception then write the code to close that file . 2.Unload files is loaded if any exception occurs
        print("Inside finally bloack")       

if __name__ == "__main__":
    main()    

    
    '''

    try : code may return exception , run under PVM observation 
    except : handler - Catch block
    finally : always executed 

    '''