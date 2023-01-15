def main():
    print("Enter number")
    no = int(input())

    i=1
    print("Factors are:")
    while(i <= int(no/2)):
        if(no % i == 0):
            print(i)
        i = i + 1 # statement should be in loop and out of if statement


if __name__ == "__main__":
    main()