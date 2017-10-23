import os

sudo_mode = "sudo "

def python_bluez_installer():
    cmd = sudo_mode + "apt-get install python-bluez"
    cmd_result=os.system(cmd);
    
    if cmd_result == 0:
        print("Python Bluez Module is installed!")

def daemon_comp():
    cmd = sudo_mode + "cp dbus-org.bluez.service -t /etc/systemd/system"
    cmd_result=os.system(cmd);
    if cmd_result == 0:
        print("Bluetooth Daemon is in compatibility mode!")
        
def load_serial_port():
    cmd = sudo_mode + "sdptool add SP"
    cmd_result=os.system(cmd);
    
    if cmd_result == 0:
        print("Serial port profile loaded!")

def change_device_name():
    cmd = sudo_mode+"echo 'PRETTY_HOSTNAME=rpi' > /etc/machine-info"
    cmd_result=os.system(cmd);
    
    if cmd_result == 0:
        print("Device name is changed! Now restarting Bluetooth!")
        os.system("sudo service bluetooth restart")

def set_up_bl():
    cmd = sudo_mode+"bluetoothctl <<EOF\npower on\ndiscoverable on\npairable on\nagent NoInputNoOutput\ndefault-agent\nEOF"
    cmd_result=os.system(cmd);
    
    if cmd_result == 0:
        print("Bluetooth is configured! Now restarting dhcpcd!")
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