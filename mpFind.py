import sys
from modules import helperFunctions
from modules import nmapper

def main():
    try:
        helperFunctions.splash()
        gateway = nmapper.host()

        if(len(sys.argv) > 1):
            nmapper.NmapScan(sys.argv[1])
        else:
            raise Exception()
    except:
        helperFunctions.bad_splash(gateway)


if __name__ == "__main__":
    main()