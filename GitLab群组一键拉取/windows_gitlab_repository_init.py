import subprocess

name = input('请输入项目名称：')

subprocess.call(f'git clone http://zhouxingjian:123qweasdzxc@192.168.11.84/{name}/deviceservice.git',shell=True)

subprocess.call(f'git clone http://zhouxingjian:123qweasdzxc@192.168.11.84/{name}/deviceshadow.git',shell=True)

subprocess.call(f'git clone http://zhouxingjian:123qweasdzxc@192.168.11.84/{name}/ui.git',shell=True)

subprocess.call(f'git clone http://zhouxingjian:123qweasdzxc@192.168.11.84/{name}/datamanager.git',shell=True)

subprocess.call(f'git clone http://zhouxingjian:123qweasdzxc@192.168.11.84/{name}/scpiservice.git',shell=True)

subprocess.call(f'git clone http://zhouxingjian:123qweasdzxc@192.168.11.84/{name}/document.git',shell=True)