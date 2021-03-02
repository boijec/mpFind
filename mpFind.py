import sys
from modules import helperFunctions
from modules import nmapper

def main(gate):
    try:
        nmapper.NmapScan(gate)
    except:
        helperFunctions.bad_splash(gateway)


if __name__ == "__main__":
    helperFunctions.splash()
    gateway = nmapper.host()

    if(len(sys.argv) > 1):
        main(sys.argv[1])
    else:
        helperFunctions.bad_splash(gateway)