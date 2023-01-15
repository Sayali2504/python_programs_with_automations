import schedule
import time
import datetime


def Task_Minute():
    print("Task based on minutes get schduled at :",datetime.datetime.now())

def Task_Hour():
    print("Task based on hour get schduled at :",datetime.datetime.now())  

def Task_Day():
    print("Task based on day get schduled at :",datetime.datetime.now())        


def main():
    print("Inside task schedular")
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minute.do(Task_Minute)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().saturday.at("21:00").do(Task_Day)


    

    while(True):
        schedule.run_pending()
        time.sleep(1) # 1 second


if __name__ == "__main__":
    main()
