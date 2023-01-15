import schedule
import time
import datetime

def Fun():
    print("Inside fun")

def main():
    print("In main")

    schedule.every(1).minute.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
