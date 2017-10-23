import os,time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

sudo_mode = "sudo "

def python_bluez_installer():
    cmd = sudo_mode + "apt-get install python-bluez"
    cmd_result=os.system(cmd);
    
    if cmd_result == 0:
        print(bcolors.OKGREEN+"Python Bluez Module is installed!"+bcolors.ENDC)

def daemon_comp():
    cmd = sudo_mode + "cp dbus-org.bluez.service -t /etc/systemd/system"
    cmd_result=os.system(cmd);
    if cmd_result == 0:
        print(bcolors.OKGREEN+"Bluetooth Daemon is in compatibility mode!"+bcolors.ENDC)
        cmd = 'systemctl daemon-reload'
        cmd_result = os.system(cmd)
        cmd = 'service bluetooth restart'
        cmd_result = os.system(cmd)
        
def load_serial_port():
    cmd = sudo_mode + "sdptool add SP"
    cmd_result=os.system(cmd);
    
    if cmd_result == 0:
        print(bcolors.OKGREEN+"Serial port profile loaded!"+bcolors.ENDC)

def change_device_name():
    cmd = sudo_mode+"echo 'PRETTY_HOSTNAME=rpi' > /etc/machine-info"
    cmd_result=os.system(cmd);
    
    if cmd_result == 0:
        print(bcolors.OKGREEN+"Device name is changed! Now restarting Bluetooth!"+bcolors.ENDC)
        cmd = 'systemctl daemon-reload'
        cmd_result = os.system(cmd)
        cmd = 'service bluetooth restart'
        cmd_result = os.system(cmd)

def set_up_bl():
    cmd = sudo_mode+"bluetoothctl <<EOF\npower on\nEOF"
    cmd_result=os.system(cmd);
    if cmd_result==0:
        print(bcolors.OKGREEN+"Bluetooth is powered on!"+bcolors.ENDC)
        time.sleep(2)
        cmd = sudo_mode+"bluetoothctl <<EOF\npairable on\ndiscoverable on\nEOF"
        cmd_result=os.system(cmd);
        if cmd_result==0:
            print(bcolors.OKGREEN+"Device is discoverable and pairable!"+bcolors.ENDC)
            time.sleep(2)
            cmd= sudo_mode+"bluetoothctl <<EOF\nagent NoInputNoOutput\nEOF"
            cmd_result=os.system(cmd)
            if cmd_result==0:
                print(bcolors.OKGREEN+"No pair key is set!"+bcolors.ENDC)
                cmd= sudo_mode+"bluetoothctl <<EOF\ndefault-agent\nEOF"
                cmd_result=os.system(cmd)
                
                cmd = 'systemctl daemon-reload'
                cmd_result = os.system(cmd)
                print cmd + " - " + str(cmd_result)

                cmd = 'systemctl restart dhcpcd'
                cmd_result = os.system(cmd)
                print cmd + " - " + str(cmd_result)


python_bluez_installer()
daemon_comp()
load_serial_port()
change_device_name()
set_up_bl()