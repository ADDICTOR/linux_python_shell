import subprocess

linux_passward = ["123qweasdzxc"]

# path = input("请输入群组安装路径")

# subprocess.call(f'cd {path}',shell=True)

subprocess.call(f'echo {linux_passward} | sudo -S touch /home/.git-credentials')

subprocess.call(f'echo {linux_passward} | sudo -S vim /home/.git-credentials')

