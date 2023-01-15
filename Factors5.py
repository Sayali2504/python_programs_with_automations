from Numbers import *
from sys import *

#argv[0] - contains file name
def main():
    print("Application name is :",argv[0])
    DisplayFactors(int(argv[1]))

if __name__ == "__main__":
    main()