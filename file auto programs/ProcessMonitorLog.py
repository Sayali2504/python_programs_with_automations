# python abc.py Data(folder name for logfiles to store)
#to create log file 

#time.ctime / time.time / datetime.datetime

import time
import sys
import psutil
import os

import schedule


def ProcessDisplay(log_dir = "Marvellous"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = "-"*80
    log_path =os.path.join(log_dir,"MarvellousLog%s.log"%(str(time.localtime())))
    f = open(log_path, mode="w", encoding='utf-8')
    f.write(seperator+"\n")
    f.write("Marvellous Infosystem Process Logger : "+time.ctime()+" \n")
    f.write(seperator+"\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms']=proc.memory_info().vms/(1024*1024) #to display in MB 1024 * 1024
            listprocess.append(pinfo)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

def TasK():
    ProcessDisplay(sys.argv[1])


def main():
    print("----------- Sayali Balkawade Automations -----------")

    print("Automation script started with name : ",sys.argv[0])

    if(len(sys.argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if((sys.argv[1] == "-h") or (sys.argv[1] == "-H")):
        print("Help : This script is used to log record of running processes")
        exit()

    if((sys.argv[1] == "-u") or (sys.argv[1] == "-U")):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(1).minute.do(TasK)

        while True:
            schedule.run_pending()
            time.sleep(60)


    except ValueError:
        print("Error : Invalid Data Type Input")

    except Exception:
        print("Error :invalid input ")


if __name__ == "__main__":
    main()