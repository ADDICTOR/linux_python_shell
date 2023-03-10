import os
import subprocess

name = input('请输入项目名称：')

username = 'zhouxingjian'

password = '123qweasdzxc'

repository_list = ['deviceservice','deviceshadow','ui','datamanager','scpiservice','document','modbusserver','susi4']

submodule_list = ['deviceservice','deviceshadow']

command = f"git clone http://{username}:{password}@192.168.11.84/{name}/"

path =os.getcwd()

for r in repository_list:
    subprocess.call(f"{command}{r}.git",shell=True)
    # subprocess.call(f"cd {r}",shell=True)
    # subprocess.call(f"git submodule init | git submodule update",shell=True)

for s in submodule_list:
    subprocess.call("git submodule init",shell=True,cwd=f"{path}\{s}")
    subprocess.call("git submodule update",shell=True,cwd=f"{path}\{s}")