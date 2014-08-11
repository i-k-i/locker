#!/usr/bin/python


import pyudev, sys


from datetime import datetime



def log(level, msg):


    #strToWrite = str(datetime.now()) + ":" + str(msg)


    i = 0


    strToWrite = ""


    while True:


        if (i >= level):


            break


        strToWrite = strToWrite + "  "


        i = i + 1


    strToWrite = strToWrite + str(msg)


    print strToWrite



def getInfoForADevice(aDevice, level):


    msgStr = "*****************************************************"


    log(level, msgStr)


    msgStr = "sys_path: %s:" % aDevice.sys_path


    log(level, msgStr)


    msgStr = "device_path: " + aDevice.device_path


    log(level, msgStr)


    msgStr = "sys_name: " + aDevice.sys_name


    log(level, msgStr)


    msgStr = "subsystem: " + str(aDevice.subsystem)


    log(level, msgStr)


    msgStr = "driver: " + str(aDevice.driver)


    log(level, msgStr)


    msgStr = "device type: " + str(aDevice.device_type)


    log(level, msgStr)


    msgStr = "device node: " + str(aDevice.device_node)


    log(level, msgStr)


    msgStr = "----------ATTRIBUTES----------"


    log(level, msgStr)


    for attrName, attrValue in aDevice.attributes.iteritems():


        msgStr = attrName + ": " + str(attrValue)


        log(level, msgStr)


    for aChildDevice in aDevice.children:


        getInfoForADevice(aChildDevice, level + 1)



if __name__ == '__main__':


    global context


    context = pyudev.Context()


    if (len(sys.argv) == 1):


        devices = context.list_devices(subsystem="usb") 


        #devices = context.list_devices()


        if not devices:


            print "no device found"


        for aDevice in devices:


            getInfoForADevice(aDevice, 0) 


    else:


        aDevice = pyudev.Device.from_path(context, sys.argv[1])


        getInfoForADevice(aDevice, 0)
