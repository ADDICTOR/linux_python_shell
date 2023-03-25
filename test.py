"""test
"""
# with open('./requirements.txt') as f:
#     data = f.read()
#     print(type(data))
#     print(data)


# with open('./test.txt','w') as f:
#     f.write('1\n')
#     f.write('2')

apt_source_list = []
apt_software_list = []
pip_source_list = []
python_environment_list = []


with open('./requirements.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if line == '[APT_SOURCE]\n':
            operation = apt_source_list
        elif line == '[APT_SOFTWARE]\n':
            operation = apt_software_list
        elif line == '[PIP_SOURCE]\n':
            operation = pip_source_list
        elif line == '[PIP_MODULE]\n':
            operation = python_environment_list
        else:
            operation.append(line.strip('\n'))

print(apt_source_list)
print(apt_software_list)
print(pip_source_list)
print(python_environment_list)
