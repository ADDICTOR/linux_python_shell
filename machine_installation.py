import subprocess


# apt国内源，阿里云，也可更换为其他国内源，加快下载速度
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


# 需下载软件列表
apt_software_list = ['openssh-server','x11vnc','git','supervisor','make','gcc','g++','vim','libudev-dev',
                    'autoconf','libzmq3-dev','chrome-gnome-shell','libzmq3-dev','net-tools']


pip_source = 'https://pypi.tuna.tsinghua.edu.cn/simple'


# python需要安装的环境，目前主流linux系统都自带python3
python_environment_list = ['flask','pyautogui==0.9.52','pyqtgraph==0.12.2','PyQt==5.14.2','PyQtWebEngine==5.14.0',
                            'pymongo==3.8.0','pyserial','paho-mqtt','grpcio_tools','protobuf','grpcio','pyzmq',
                            'python-xlib','modbus_tk','influxdb_client','pypattyrn','Pint','pyinstaller']


# 用户密码
password = '123456'


def apt_switching_source():
    """apt更换国内源
    """
    subprocess.call(f'echo {password} | sudo -S cp /etc/apt/sources.list /etc/apt/sources.list.bat', shell=True)
    with open('./sources.list', 'w') as f:
        f.writelines(apt_sources_list)
    subprocess.call(f'echo {password} | sudo -S apt-get update', shell=True)
    subprocess.call(f'echo {password} | sudo -S apt-get upgrade', shell=True)


def apt_software_installation():
    """apt换源后软件下载
    """
    for s in apt_software_list:
        subprocess.call(f'sudo -S apt-get install {s} -y', shell=True)


def pip_switching_source():
    """pip更换国内源
    """
    subprocess.call(f'pip3 config set global.index-url {pip_source}',shell=True)


def python_environment_installation():
    """pip安装python环境
    """
    for p in python_environment_list:
        subprocess.call(f'pip3 install {p}', shell=True)

if  __name__ == "__main__":
    apt_switching_source()
    apt_software_installation()
    pip_switching_source()
    python_environment_installation()