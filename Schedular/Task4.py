import schedule
import time
import datetime
import sys

def Task_Minute():
    print("Task based on minutes get schduled at :",datetime.datetime.now())

def Task_Hour():
    print("Task based on hour get schduled at :",datetime.datetime.now())  

def Task_Day():
    print("Task based on day get schduled at :",datetime.datetime.now())        

def Schedule_close():
    sys.exit()

def main():
    print("Inside task schedular")
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minute.do(Task_Minute)
    schedule.every(2).minutes.do(Schedule_close)

    while(True):
        schedule.run_pending()
        time.sleep(1) # 1 second


if __name__ == "__main__":
    main()
