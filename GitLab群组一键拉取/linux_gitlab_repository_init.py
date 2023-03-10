import subprocess

name = input("请输入项目名称：") 

linux_passward = ["123qweasdzxc"]

username = ["zhouxingjian"]

password = ["123qweasdzxc"]

subprocess.call(f'echo {linux_passward} | sudo -S touch /home/.git-credentials')

with open('/home/.git-credentials','w') as f:
    f.write(f'https://{username[0]}:{password[0]}@192.168.11.84')

subprocess.call(f'git config --global credential.helper store', shell=True)

subprocess.call(f'git clone http://192.168.11.84/{name}/deviceservice.git',shell=True)

subprocess.call(f'git clone http://192.168.11.84/{name}/deviceshadow.git',shell=True)

subprocess.call(f'git clone http://192.168.11.84/{name}/ui.git',shell=True)

subprocess.call(f'git clone http://192.168.11.84/{name}/datamanager.git',shell=True)

subprocess.call(f'git clone http://192.168.11.84/{name}/scpiservice.git',shell=True)

subprocess.call(f'git clone http://192.168.11.84/{name}/document.git',shell=True)