import subprocess


apt_sources_list = ['deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse\n',
            'deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse\n',
            'deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse\n',
            'deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse\n',
            'deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse\n',
            'deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse\n',
            'deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse\n',
            'deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse\n',
            'deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse\n',
            'deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse]\n']


apt_software_list = ['openssh-server','x11vnc','git','supervisor','make','gcc','g++','vim','libudev-dev','autoconf','libzmq3-dev']


python_environment_list = []

passward = '123456'


def apt_switching_source():
    """apt更换国内源
    """
    subprocess.call('sudo cp /etc/apt/sources.list /etc/apt/sources.list.bat', shell=True)
    with open('./sources.list', 'w') as f:
        f.writelines(apt_sources_list)
    subprocess.call('sudo apt-get update', shell=True)
    # subprocess.call(f'echo {password} | sudo -S apt-get update')
    subprocess.call('sudo apt-get upgrade', shell=True)


def apt_software_installation():
    """apt换源后软件下载
    """
    software_str = ','.join(apt_software_list)
    subprocess.call(f'sudo apt-get install {software_str}', shell=True)


def python_environment_installation():
    """pip环境安装
    """
    # subprocess.call(f'pip install {python_environment_list}', shell=True)

if  __name__ == "__main__":
    apt_switching_source()
    apt_software_installation()
    python_environment_installation()