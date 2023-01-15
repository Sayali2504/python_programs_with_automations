from sys import *

import psutil

#psutil.process_iter() -> we can get process id, username,name,virtual address , main thread , other threads 

def ProcessDisplay():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])

            listprocess.append(pinfo)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess): #trek bag example  for except block
            pass

    return listprocess

def main():
    print("----------- Sayali Balkawade Automations -----------")

    print("Automation script started with name : ",argv[0])

    listprocess=ProcessDisplay()

    for element in listprocess:
        print(element)

if __name__ == "__main__":
    main()