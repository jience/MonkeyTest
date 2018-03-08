from androguard.core import androconf
from androguard.core.bytecodes import apk

def get_app_packagename(app_path):
    appinfo = _get_app_info(app_path)
    if appinfo==None:
        return None
    packagename = _get_apk_package(appinfo)
    return packagename

def _get_app_info(app_path):
    apkinfo = apk.APK(app_path)
    if(androconf.is_android(app_path)=='APK' and apkinfo.is_valid_APK()):
        return apkinfo
    return None

def _get_apk_package(app_info):
    package = app_info.get_package()
    return package
