import re
import os
import pandas
import mysql.connector as mc

def get_russian_in_file(dir):
    file = open(dir, 'r', encoding='utf-8')
    data = file.read()
    result = re.findall("[цукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ]+", data)
    result = [x for x in result if x != '']
    return result
def get_data_from_bd():
    all_data = []
    cnx = mc.connect(host='185.125.44.222', user='pwa-admin', password='}Q2yF{M;$w852}37', database='pwa', auth_plugin='mysql_native_password')
    curs = cnx.cursor()
    query = 'SELECT * FROM pwa.localization;'
    curs.execute(query)
    result = curs.fetchall()
    file = open('test2.txt', 'w')
    for i in result:
        sent = i[2]
        print(sent)
        file.write('"'+i[1]+'"'+': '+'"'+i[2]+'"'+',\n')
    file.close()
def get_all_images(dirname):
    path = dirname
    all_data = []
    # we shall store all the file names in this list
    filelist = []

    for root, dirs, files in os.walk(path):
        for file in files:
            # append the file name to the list
            filelist.append(os.path.join(root, file))

    # print all the file names
    for name in filelist:
        try:
            if name.endswith('.png'):
                all_data.append(name.split('C:/Users/Danil/WebstormProjects/')[1])
            elif name.endswith('.svg'):
                all_data.append(name.split('C:/Users/Danil/WebstormProjects/')[1])
            elif name.endswith('.jpg'):
                all_data.append(name.split('C:/Users/Danil/WebstormProjects/')[1])
            elif name.endswith('.ico'):
                all_data.append(name.split('C:/Users/Danil/WebstormProjects/')[1])
        except:
            pass
    file = open('test1.txt', 'w')
    for i in all_data:
        file.write(i + ',\n')
    file.close()

def get_all_files(dirname):
    path = dirname
    all_data = []
    # we shall store all the file names in this list
    filelist = []

    for root, dirs, files in os.walk(path):
        for file in files:
            # append the file name to the list
            filelist.append(os.path.join(root, file))

    # print all the file names
    for name in filelist:
        try:
            res = get_russian_in_file(name)
            if res != []:
                print(name.split('C:/Users/Danil/WebstormProjects/')[1])
                all_data.append(name.split('C:/Users/Danil/WebstormProjects/')[1])
        except:
            pass
    print(all_data)
    file = open('test.txt', 'w')
    for i in all_data:
        file.write(i+'\n')
    file.close()


get_all_files('C:/Users/Danil/WebstormProjects/iqos-pwa')
