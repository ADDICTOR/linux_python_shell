import os
import subprocess

username = 'zhouxingjian'

password = '123qweasdzxc'

driver_list = ['fx3_usbdriver','tunkiaprotocol','unit_converter']

command = f"git clone http://{username}:{password}@192.168.11.84/driver/"

path =os.getcwd()

# 建立驱动目录
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
subprocess.call("cp lib/libcyusb.so /usr/lib/",shell=True,cwd=f"{path}/driver/{driver_list[0]}/cyusb_linux_1.0.5")
subprocess.call("cp lib/libcyusb.so.1 /usr/lib/",shell=True,cwd=f"{path}/driver/{driver_list[0]}/cyusb_linux_1.0.5")

# TODO 研究清楚cp .so .so.1 到 /usr/lib的意义
# TODO 是否需要进一步make

# TunkiaProtocol
subprocess.call(f"python3 setup.py sdist",shell=True,cwd=f"{path}/driver/{driver_list[1]}")
subprocess.call(f"python3 setup.py install",shell=True,cwd=f"{path}/driver/{driver_list[1]}")

# unit_converter
subprocess.call(f"python3 setup.py sdist",shell=True,cwd=f"{path}/driver/{driver_list[2]}")
subprocess.call(f"python3 setup.py install",shell=True,cwd=f"{path}/driver/{driver_list[2]}")