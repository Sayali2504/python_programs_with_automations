#import Numbers
#from Numbers import DisplayFactors
#from Numbers import *
import Numbers as NUM
def main():
    print("Enter number")
    No = int(input())

    NUM.DisplayFactors(No) #for line 4
    #DisplayFactors(No) #for lime 2 ,3 
    #Numbers.DisplayFactors(No) #for 1

if __name__ == "__main__":
    main()