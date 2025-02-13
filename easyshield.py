import os
import time
import psutil
import ctypes
from datetime import datetime

class EasyShield:
    def __init__(self, block_list):
        self.block_list = block_list
        self.log_file = "blocked_apps_log.txt"

    def block_applications(self):
        while True:
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] in self.block_list:
                    self.kill_process(process.info['pid'], process.info['name'])
            time.sleep(5)  # Check every 5 seconds

    def kill_process(self, pid, app_name):
        try:
            os.kill(pid, 9)
            self.log_blocked_application(app_name)
            print(f"Blocked and terminated {app_name}")
        except Exception as e:
            print(f"Error terminating {app_name}: {e}")

    def log_blocked_application(self, app_name):
        with open(self.log_file, "a") as log:
            log.write(f"{datetime.now()}: Blocked {app_name}\n")

def enable_privileges():
    # Enable the SeDebugPrivilege to allow the script to terminate any process
    try:
        hToken = ctypes.c_void_p()
        TOKEN_ALL_ACCESS = 0xF01FF
        ctypes.windll.advapi32.OpenProcessToken(ctypes.windll.kernel32.GetCurrentProcess(), TOKEN_ALL_ACCESS, ctypes.byref(hToken))

        class LUID(ctypes.Structure):
            _fields_ = [("LowPart", ctypes.c_ulong), ("HighPart", ctypes.c_long)]

        class LUID_AND_ATTRIBUTES(ctypes.Structure):
            _fields_ = [("Luid", LUID), ("Attributes", ctypes.c_ulong)]

        class TOKEN_PRIVILEGES(ctypes.Structure):
            _fields_ = [("PrivilegeCount", ctypes.c_ulong), ("Privileges", LUID_AND_ATTRIBUTES * 1)]

        privilege = TOKEN_PRIVILEGES()
        privilege.PrivilegeCount = 1
        privilege.Privileges[0].Attributes = 0x00000002  # SE_PRIVILEGE_ENABLED

        ctypes.windll.advapi32.LookupPrivilegeValueA(None, b'SeDebugPrivilege', ctypes.byref(privilege.Privileges[0].Luid))
        ctypes.windll.advapi32.AdjustTokenPrivileges(hToken, False, ctypes.byref(privilege), 0, None, None)
        return True
    except Exception as e:
        print(f"Failed to enable privileges: {e}")
        return False

if __name__ == "__main__":
    if not enable_privileges():
        print("Could not set necessary privileges. Please run as administrator.")
    else:
        block_list = ['notepad.exe', 'calc.exe']  # Add application names you want to block
        shield = EasyShield(block_list)
        shield.block_applications()