import sys

logfile=open('/locker/usb_act.log','a')
logfile.write(str(sys.argv))
logfile.write('\n')
logfile.close()
