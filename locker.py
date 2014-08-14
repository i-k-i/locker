#!/usr/bin/python

import time
import sys
import random
import subprocess
import os
import sqlite3

arglist=sys.argv

devpath = arglist[-1]
devname = arglist[-2]
mountdir = '/mnt/locker/'

def fsinterfase(devname, key=''):
    def readkey(mountpoint):
        keypath = os.path.join(mountpoint,'key')
        if os.path.isfile(keypath):
            keyfile = open(keypath)
            greenkey = keyfile.readline(keyfile)
            keyfile.close()
            return greenkey

    def writekey(mountpoint,key):
        keypath = os.path.join(mountpoint,'key')
        if os.path.isfile(keypath):
            keyfile = open(keypath,'w')
            keyfile.write(key)
            keyfile.close()

    while True:
        mpname = str(random.randint(10**3,10**4))
        if mpname not in os.listdir(mountdir):
            mountpoint = os.path.join(mountdir,mpname)
            os.mkdir(mountpoint)
            break
    subprocess.Popen("/bin/mount {} {}".format(devname, mountpoint))
    if key == '':
        key = readkey(mountpoint)
    else:
        writekey(mountpoint,key)
    subprocess.Popen("/bin/umount {}".format(mountpoint))


def dbconnector(devpath, devname, key = ''):
    conn = sqlite3.connect('/locker/locker.db')

    cur = conn.cursor()

    cur.execute('''INSER INTO 
    ''')



class dbconnector():


if __name__ = '__main__':
    mounter()