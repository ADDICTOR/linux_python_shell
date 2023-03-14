import subprocess


# apt国内源，阿里云，也可更换为其他国内源，加快下载速度
apt_source_list = []
# 需下载软件列表
apt_software_list = []
# pip国内源
pip_source_list = []
# python需要安装的环境，目前主流linux系统都自带python3
python_environment_list = []
# 用户密码
password = []


def config_initialization():
    """配置文件读取，这种思路可以用在很多东西上面
    """
    with open('./requirements.txt', 'r') as f:
        for line in f.readlines():
            if line == '[APT_SOURCE]\n':
                operation = apt_source_list
                continue
            elif line == '[APT_SOFTWARE]\n':
                operation = apt_software_list
                continue
            elif line == '[PIP_SOURCE]\n':
                operation = pip_source_list
                continue
            elif line == '[PIP_MODULE]\n':
                operation = python_environment_list
                continue
            elif line == '[PASSWORD]\n':
                operation = password
                continue
            else:
                operation.append(line.strip('\n'))


def apt_switching_source():
    """apt更换国内源
    """
    subprocess.call(f'echo {password[0]} | sudo -S cp /etc/apt/sources.list /etc/apt/sources.list.bat', shell=True)
    with open('./sources.list', 'w') as f:
        for s in apt_source_list:
            f.write(f'{s}\n')
    subprocess.call(f'echo {password[0]} | sudo -S apt-get update', shell=True)
    subprocess.call(f'echo {password[0]} | sudo -S apt-get upgrade', shell=True)


def apt_software_installation():
    """apt换源后软件下载
    """
    for s in apt_software_list:
        subprocess.call(f'sudo -S apt-get install {s} -y', shell=True)


def pip_switching_source():
    """pip更换国内源
    """
    subprocess.call(f'pip3 config set global.index-url {pip_source_list[0]}',shell=True)


def python_environment_installation():
    """pip安装python环境
    """
    for p in python_environment_list:
        subprocess.call(f'pip3 install {p}', shell=True)

if  __name__ == "__main__":
    config_initialization()
    apt_switching_source()
    apt_software_installation()
    pip_switching_source()
    python_environment_installation()