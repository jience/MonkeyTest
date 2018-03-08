import os  
import tempfile  
import re  
  
tempFile = tempfile.gettempdir()

def install_app(device,app_path):
    cmd = "adb -s " + device +  " install -r  " + app_path
    print(cmd)
    os.popen(cmd)

def uninstall_app(device,packagename):
    cmd = "adb -s " + device +  " uninstall " + packagename
    print(cmd)
    os.popen(cmd)

def check_app_installed(devicename,package_name):
    cmd = "adb -s  " + devicename + "  shell pm list packages -f " + package_name
    cmdoutput = os.popen(cmd).readlines()

    for line in cmdoutput:
        if "package" in line and "=" in line:
            installedpackage = line[line.index('=')+1:len(line)-1]
            if installedpackage == package_name:
                return True
    return False

def get_serialno(device):
    serialno = os.popen("adb -s " + device + " shell getprop ro.serialno ").readline()
    return serialno

def get_devices():
    devicelist=[]
    output = os.popen("adb devices")
    while True:
        line = output.readline()
        if line == None or line == "":
            break
        if "devices" in line:
            continue
        device = []
        if "device" in line:
            devicename = line[0:line.find('device')]
            serialno = get_serialno(devicename)
            device.append(devicename)
            device.append(serialno)
            devicelist.append(device)
    return devicelist

def get_aapt():  
    if "ANDROID_HOME" in os.environ:  
        rootDir = os.path.join(os.environ["ANDROID_HOME"], "build-tools")  
        for path, subdir, files in os.walk(rootDir):  
            if "aapt.exe" in files:  
                return os.path.join(path, "aapt.exe")  
    else:  
        return "ANDROID_HOME not exist"  
  
def get_current_package_name():  
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")  
    os.popen("adb wait-for-device")  
    out = os.popen("adb shell dumpsys input | findstr FocusedApplication").read()  
    package_name = pattern.findall(out)[0].split("/")[0]  
  
    return package_name  
  
def get_match_apk(package_name):  
    list = []  
    for packages in os.popen("adb shell pm list packages -f " + package_name).readlines():  
        list.append(packages.split(":")[-1].split("=")[0])  
    apk_name = list[0].split("/")[-1]  
    os.popen("adb pull " + list[0] + " " + tempFile)  
  
    return tempFile + "\\" + apk_name  
