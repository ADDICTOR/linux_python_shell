import os
import subprocess

username = 'zhouxingjian'

password = '123qweasdzxc'

# repository_list = ['deviceservice','deviceshadow','ui','datamanager','scpiservice','document','modbusserver','susi4']

# submodule_list = ['deviceservice','deviceshadow']

driver_list = ['fx3_usbdriver','tunkiaprotocol','unit_converter']

command = f"git clone http://{username}:{password}@192.168.11.84/driver/"

path =os.getcwd()

# for r in repository_list:
#     subprocess.call(f"{command}{r}.git",shell=True)
#     # subprocess.call(f"cd {r}",shell=True)
#     # subprocess.call(f"git submodule init | git submodule update",shell=True)

# for s in submodule_list:
#     subprocess.call("git submodule init",shell=True,cwd=f"{path}\{s}")
#     subprocess.call("git submodule update",shell=True,cwd=f"{path}\{s}")

subprocess.call("mkdir driver", shell=True)

for d in driver_list:
    subprocess.call(f"{command}{d}.git",shell=True,cwd=f"{path}/driver")

# libusb
subprocess.call("./configure",shell=True,cwd=f"{path}/diver/{driver_list[0]}/libusb-1.0.25")
subprocess.call("make",shell=True,cwd=f"{path}/diver/{driver_list[0]}/libusb-1.0.25")
subprocess.call("sudo make install",shell=True,cwd=f"{path}/diver/{driver_list[0]}/libusb-1.0.25")

# libcyusb
subprocess.call("make",shell=True,cwd=f"{path}/driver/{driver_list[0]}/cyusb_linux_1.0.5")
subprocess.call("sudo install.sh",shell=True,cwd=f"{path}/driver/{driver_list[0]}/cyusb_linux_1.0.5")
subprocess.call("cp lib/libcyusb.so /usb/lib/",shell=True,cwd=f"{path}/driver/{driver_list[0]}/cyusb_linux_1.0.5")
subprocess.call("cp lib/libcyusb.so.1 /usb/lib/",shell=True,cwd=f"{path}/driver/{driver_list[0]}/cyusb_linux_1.0.5")

# TunkiaProtocol
subprocess.call(f"python3 setuo.py sdist",shell=True,cwd=f"{path}/driver/{driver_list[1]}")
subprocess.call(f"python3 setuo.py install",shell=True,cwd=f"{path}/driver/{driver_list[1]}")

# uni_converter
subprocess.call(f"python3 setuo.py sdist",shell=True,cwd=f"{path}/driver/{driver_list[2]}")
subprocess.call(f"python3 setuo.py install",shell=True,cwd=f"{path}/driver/{driver_list[2]}")