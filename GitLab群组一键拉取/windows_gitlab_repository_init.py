import subprocess

path = input("请输入群组安装路径")

subprocess.call(f'cd {path}',shell=True)

