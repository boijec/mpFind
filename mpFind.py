#The Programmable user interface is found at the bottom of the code
import nmap
import os
import time
import socket
import sys
import subprocess
import datetime
import getpass

now = datetime.datetime.now()

#function to append to the logfile
def log(message):
    currentLogName = now.strftime("logs\%Y%m%d-log.txt")
    timeStamp = now.strftime("%Y-%m-%d %H:%M ->")
    log = open(currentLogName, "a")
    log.write("%s %s" % (timeStamp, message))
    log.write(dash)
    log.close()

#animation function
def anim_print(s):
    for c in s:
        print(c, end="", flush=True)
        time.sleep(0.03)

#You can customize this to what ever start logo you want :)
def Welcome():
    print("$$\      $$\           $$$$$$$$\ $$\                 $$\ ")
    print("$$$\    $$$ |          $$  _____|\__|                $$ |")
    print("$$$$\  $$$$ | $$$$$$\  $$ |      $$\ $$$$$$$\   $$$$$$$ |")
    print("$$\$$\$$ $$ |$$  __$$\ $$$$$\    $$ |$$  __$$\ $$  __$$ |")
    print("$$ \$$$  $$ |$$ /  $$ |$$  __|   $$ |$$ |  $$ |$$ /  $$ |")
    print("$$ |\$  /$$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |$$ |  $$ |")
    print("$$ | \_/ $$ |$$$$$$$  |$$ |      $$ |$$ |  $$ |\$$$$$$$ |")
    print("\__|     \__|$$  ____/ \__|      \__|\__|  \__| \_______|")
    print("             $$ |                                        ")
    print("             $$ |                                        ")
    print("             \__|                                        ")
    print("------------------Created by: Minut3man------------------")
    print(dash)
    print("Welcome to MpFind")
    print("Making it easier to find mediaplayers over LAN")
    print("Your Default Gateway is: " + gateway)
    print("type 'help' to open help file")

#Input by the user dictates what default gateway is scanned - then outputs if mediaplayer is found
def NmapScan(action):
    action = action[1]
    BS = "BrightSign MEDIAPLAYER FOUND! - "
    SPX = "SpinetiX MEDIAPLAYER FOUND! - "
    ELSE = "NO MEDIAPLAYER FOUND... - "
    UNI = 0
    
    psc = nmap.PortScanner()
    psc.scan(hosts=action, arguments='-F')
    inputCheck = psc.command_line()
    print(dash)
    logMSG = "INPUT CHECK FROM NMAP : %s" % (inputCheck)
    log(logMSG)
    #print(inputCheck)
    for item in psc.all_hosts():
        ip = item
        hostname = psc[ip].hostname()
        serial = psc[ip].hostname()
        if 'BrightSign-' in hostname:
            serial = hostname.replace('BrightSign-', '')
            if '77D' in serial:
                model = "HD222"
            elif '78D' in serial:
                model = "HD222"
            elif '33D' in serial:
                model = "HD223"
            elif '33E' in serial:
                model = "HD223"
            elif 'L2D' in serial:
                model = "XD232"
            elif 'R3G' in serial:
                model = "XD233"
            elif 'L8G' in serial:
                model = "XT"
            elif '53D' in serial:
                model = "HS123"
            elif '53E' in serial:
                model = "HS123"
            elif '31D' in serial:
                model = "LS423"
            elif '31E' in serial:
                model = "LS423"
            else:
                model = "NOT FOUND"
            print(rowbreak)
            print("%s %s IP: %s --- SERIAL NUMBER: %s(%s) --- HOSTNAME: %s" % (tab, BS, ip, serial, model, hostname))
            print(rowbreak)
            UNI = UNI + 1
            logMSG = "BRIGHTSIGN PLAYER WAS FOUND IN SCAN!"
            log(logMSG)
        elif 'spx-hmp-' in hostname:
            serial = hostname.replace('spx-hmp-', '')
            if '5000' in serial:
                model = "HMP 100/130"
            elif '5010' in serial:
                model = "HMP 200"
            elif '5020' in serial:
                model = "HMP 300"
            else:
                model = "NOT FOUND"
            print(rowbreak)
            print("%s %s IP: %s --- SERIAL NUMBER: %s(%s) --- HOSTNAME: %s" % (tab, SPX, ip, serial, model, hostname))
            print(rowbreak)
            UNI = UNI + 1
            logMSG = "SPINETIX PLAYER WAS FOUND IN SCAN!"
            log(logMSG)
        else:
            print("%s HOSTNAME: %s --- IP: %s" % (ELSE, hostname, ip))
            UNI = UNI + 1
    print(rowbreak)
    print("--------------------------------------------")
    print("SCANNED UNIT(S) ON NETWORK: %s" % UNI)
    print(dash)
    logMSG = "PROGRAM SCANNED %s AND FOUND %s UNITS" % (action, UNI)
    log(logMSG)

def Host():
    gateway = subprocess.check_output(['ipconfig'], shell=True).decode('ISO-8859-1')
    gateway = gateway[gateway.find('Gateway'):]
    gateway = gateway[gateway.find(':'):][2:]
    gateway = gateway[:gateway.find('\n')]
    logMSG = "FINDING DEFAULT GATEWAY : %s" % (gateway)
    log(logMSG)
    return gateway

def HostAdress():
    adress = subprocess.check_output(['ipconfig'], shell=True).decode('ISO-8859-1')
    adress = adress[adress.find('IPv4'):]
    adress = adress[adress.find(':'):][2:]
    adress = adress[:adress.find('\n')]
    return adress

#Small helpfile
def Help():
    print(dash)
    print("LIST OF COMMANDS")
    print("--------------------------")
    print("scan [target host]")
    print("clear | cls")
    print("exit | bye")
    print("mpfind")
    print("--------------------------")
    print("hint: because your default gateway is %s" % gateway)
    print("you can replace the last number(the localization number) with a '*'")
    print(dash)

#Quit message
def Quit():
    logMSG = "APPLICATION WAS CLOSED %s" % (dash)
    log(logMSG)
    print(dash)
    print("Closing connection from %s" % selfhost)
    print("Bye...")
    print(dash)

#Clearing the terminal for commands
def Cls():
    clear = lambda: os.system('cls')
    clear()

def Bad():
    print(rowbreak)
    print("Bad input try again")
    print(dash)
    
#The UI
dash = "\n"
tab = "\t"
rowbreak = " "
logMSG = "APPLICATION STARTED"
log(logMSG)

selfhost = socket.gethostname()
logMSG = "GETTING HOSTNAME : %s" % (selfhost)
print(logMSG)
log(logMSG)

self = socket.gethostbyname(selfhost)
logMSG = "GETTING IP FROM HOSTNAME : %s" % (self)
print(logMSG)
log(logMSG)

sys_user = os.getenv('username')
sys_username = sys_user.upper()
logMSG = "GETTING LOGIN SESSION FROM HOSTNAME : %s" % (self)
print(logMSG)
log(logMSG)

#self = HostAdress()
gateway = Host()
print("DEFAULT GATEWAY IS : %s" % gateway)

print(rowbreak)
print(rowbreak)

inputString = "%s@%s~$: " % (selfhost, self)

Welcome()
while True:
    action = input(inputString)
    logMSG = "LOGGED USER COMMAND : %s" % (action)
    log(logMSG)
    action = action.lower()
    action = action.split()
    #action = input(selfhost + "@" + self + "~$: ")

    try:
        if 'scan' in action:
            NmapScan(action)
        elif(action[0] == 'exit' or action[0] == 'bye'):
            Quit()
            break
        elif(action[0] == 'help'):
            Help()
        elif(action[0] == 'clear' or action[0] == 'cls'):
            Cls()
        elif(action[0] == 'mpfind'):
            Welcome()
        else:
            Bad()
    except:
        Bad()
