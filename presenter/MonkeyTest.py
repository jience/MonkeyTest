import os
import subprocess
import time
from PyQt5.QtCore import pyqtSignal, Qt, QObject
from adb.adb import check_app_installed, install_app, uninstall_app

class MonkeyTest(QObject):

    signalprogressmax = pyqtSignal(int)
    signalprogresscur = pyqtSignal(int)
    signalresult = pyqtSignal(int)

    def __init__(self,mainWidget,deviceBarWidget,devicename,serialno,
                 testCount,apkpath,packagename,installapp,uninstallapp):

        super(MonkeyTest,self).__init__()

        self.lasttime = 0
        self.progress = 0
        self.max = int(testCount)
        self.deviceBar = deviceBarWidget
        self.mainBar = mainWidget
        self.devicename = devicename
        self.serialno = serialno[0:len(serialno)-1]
        self.apkpath = apkpath
        self.packagename = packagename
        self.installapp = installapp
        self.uninstallapp = installapp and uninstallapp

        self.signalprogressmax[int].connect(self.deviceBar.setProgressMax)
        self.signalprogresscur[int].connect(self.deviceBar.setProgress)
        self.signalresult[int].connect(self.mainBar.onResult)


    def startMonkeyTest(self,main,id,cmd,packagename):
        shellcmd = cmd
        os.popen("adb -s " + self.devicename + " logcat -c")
        self.nowtime = time.strftime("%Y%m%d%I%M%S")
        self.monkeyLog()
        self.monkeyErrorLog()
        self.installApp()

        if packagename != None and packagename != "":
            installed = check_app_installed(self.devicename,packagename)
            print("installed ",installed)
            if installed:
                shellcmd = " -p " + packagename + shellcmd

        self.monkeyTestThread(shellcmd)
        self.uninstallApp()
        self.signalresult.emit(id)

    def monkeyLog(self):
        filename ="log/" + self.serialno + "_" + self.nowtime + "_log.txt"
        logcat_file = open(filename, 'w')
        logcmd = "adb -s " + self.devicename + " logcat -v time"
        self.Poplog = subprocess.Popen(logcmd,stdout=logcat_file,stderr=subprocess.PIPE)

    def monkeyErrorLog(self):
        filename ="log/" + self.serialno  + "_" + self.nowtime + "_errlog.txt"
        logcat_file = open(filename, 'w')
        logcmd = "adb -s " + self.devicename + " logcat -v time *:E"
        self.Poperrorlog = subprocess.Popen(logcmd,stdout=logcat_file,stderr=subprocess.PIPE)

    def monkeyTestThread(self,cmd):
        count = 0
        monkeycmd = "adb -s " + self.devicename + " shell monkey " + cmd
        print(monkeycmd)
        self.signalprogressmax[int].emit(self.max)
        cmdoutput = os.popen(monkeycmd)

        while True:
            t = time.time()
            time.sleep(0.01)
            line = cmdoutput.readline()
            linecount = line.count("Sending")
            if linecount>0:
                count = count + linecount
                self.lasttime = t
            if self.lasttime !=0 and t - self.lasttime>5:
                count = self.max
            time.sleep(0.01)
            self.signalprogresscur[int].emit(count)
            if count >= self.max:
                break
        self.Poplog.terminate()
        self.Poperrorlog.terminate()

    def installApp(self):
        if self.installapp and self.apkpath!=None and self.apkpath !="":
            install_app(self.devicename,self.apkpath)
            time.sleep(5)

    def uninstallApp(self):
        if self.uninstallapp and self.packagename!=None and self.packagename !="":
            uninstall_app(self.devicename,self.packagename)
