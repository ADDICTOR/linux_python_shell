import subprocess

name = input('请输入项目名称：')

username = 'zhouxingjian'

password = '123qweasdzxc'

repository_list = ['deviceservice','deviceshadow','ui','datamanager','scpiservice','document','modbusserver','susi4']

command = f"git clone http://{username}:{password}@192.168.11.84/{name}/"

for r in repository_list:
    subprocess.call(f'{command}{r}.git',shell=True)