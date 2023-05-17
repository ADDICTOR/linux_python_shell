#!/bin/bash
# Ipc module packaging shell script
echo "Do you want package all modules ?(y/n)"
read key
path=`pwd`
module_list=(deviceservice deviceshadow ui datamanager scpiserver)
if [ $key == 'y']; then
    for NUM in ${module_list[*]}
    do
        cd $path
        cd ./$NUM
        pyinstaller -y app.spec
        cp ./dist/app/config/setup_example.ini ./dist/app/config/setup.ini
        sudo cp -r ./dist/app /etc/marmot/$NUM
    done
elif [ $key == 'n']; then
    echo "Please input the module name: "
    read name
    if echo "${module_list[@]}" | grep -w "$name" &>/dev/null; then
        cd ./$name
        pyinstaller -y app.spec
        cp ./dist/app/config/setup_example.ini ./dist/app/config/setup.ini
        echo 123456 | sudo cp -r ./dist/app /etc/marmot/$NUM
    else
        echo "module $name do not exist!"
    fi
else
    echo "Invalid input!"
fi