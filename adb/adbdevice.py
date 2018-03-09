import os

__author__ = 'ed'


class device:
    def __init__(self):
        self.serialno = ""
        self.devicename = ""


class adbdevice:
    def get_serialno(self, device):
        serialno = os.popen("adb -s " + device + " shell getprop ro.serialno ").readline()
        return serialno

    def get_devices(self):
        self.devicelist = []
        output = os.popen("adb devices")
        while True:
            line = output.readline()
            if line is None or line == "":
                break
            if "devices" in line:
                continue
            dev = device()
            if "device" in line:
                dev.devicename = line[0:line.find('device')]
                dev.serialno = self.get_serialno(dev.devicename)
                dev.devicename = dev.devicename.replace("\n", "")
                dev.devicename = dev.devicename.replace("\t", "")
                dev.serialno = dev.serialno.replace("\n", "")
                dev.serialno = dev.devicename.replace("\t", "")

                if len(dev.devicename) < 24:
                    for i in range(24 - len(dev.devicename)):
                        dev.devicename = dev.devicename + " "
                elif len(dev.devicename) > 24:
                    dev.devicename = dev.devicename[0:23]

                if len(dev.serialno) < 24:
                    for i in range(24 - len(dev.serialno)):
                        dev.serialno = dev.serialno + " "
                elif len(dev.serialno) > 24:
                    dev.serialno = dev.serialno[0:23]

                self.devicelist.append(dev)
