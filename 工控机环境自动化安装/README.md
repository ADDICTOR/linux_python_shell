# linux_python_shell

## linux_machine_env

工控机项目1.0版本，用于linux ubuntu / raspberry 系统的环境配置脚本，包含：

1. apt更换国内源。(Attention! APT源必须对应系统版本，linux系统请使用 uname -a / uname -m 查询)
  [Raspbian 软件仓库镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/)
2. apt换源后软件下载。
3. pip环境安装.

2.0版本，新增：

1. pip更换国内源。
2. 自动输入用户密码。
3. 自动键入'Y'.

3.0版本，新增：(ing...)

1. 读取配置文件 requirements.txt。
2. apt_source源参考

## 使用指南

1. 参考apt_source源手册
2. 配置reuirements.txt文件
    1. [APT_SOURCE] : apt国内源，更换为其他国内源，加快下载速度
    2. [APT_SOFTWARE] : 需下载软件列表，通过apt下载
    3. [PIP_SOURCE] : pip国内源
    4. [PIP_MODULE] : python需要安装的环境，目前主流linux系统都自带python3
    5. [PASSWORD] : Linux用户密码
3. 运行linux_machine_env.py

## Tips

1. chrome-gnome-shell 安装时间太久，建议单独安装
2. PyQt5==5.14.2 安装失败概率很大
