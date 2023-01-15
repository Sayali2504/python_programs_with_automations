#Application to find out the maximum number


def Maximum(no1,no2):
    if no1 > no2:
        return no1
    else:
        return no2    

def main():

    print("Enter First NUmber : ")
    value1 = input()

    print("Enter Second Number : ")
    value2 = input()

    ans = Maximum(int(value1),int(value2))

    print("Largest number is :",ans)



if __name__ == "__main__":
    main()