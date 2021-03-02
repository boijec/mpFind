import nmap
import subprocess

def NmapScan(agrumentIP):
    BS = "BrightSign MEDIAPLAYER FOUND! - "
    SPX = "SpinetiX MEDIAPLAYER FOUND! - "
    ELSE = "NO MEDIAPLAYER FOUND... - "
    UNI = 0
    
    psc = nmap.PortScanner()
    psc.scan(hosts=agrumentIP, arguments='-F')
    psc.command_line()

    if(len(psc.all_hosts()) < 1):
        raise Exception()

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
            print("\n")
            print("\t %s IP: %s --- SERIAL NUMBER: %s(%s) --- HOSTNAME: %s" % (BS, ip, serial, model, hostname))
            print("\n")
            UNI = UNI + 1
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
            print("\n")
            print("\t %s IP: %s --- SERIAL NUMBER: %s(%s) --- HOSTNAME: %s" % (SPX, ip, serial, model, hostname))
            print("\n")
            UNI = UNI + 1
        else:
            print("%s HOSTNAME: %s --- IP: %s" % (ELSE, hostname, ip))
            UNI = UNI + 1
    print("\n")
    print("--------------------------------------------")
    print("SCANNED UNIT(S) ON NETWORK: %s" % UNI)
    print("\n")

def host():
    gateway = subprocess.check_output(['ipconfig'], shell=True).decode('ISO-8859-1')
    gateway = gateway[gateway.find('Gateway'):]
    gateway = gateway[gateway.find(':'):][2:]
    gateway = gateway[:gateway.find('\n')]
    return gateway