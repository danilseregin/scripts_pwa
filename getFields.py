import pandas as pd
import mysql.connector as conn
file = 'C:/Users/Danil/Desktop/pwa_traqnslation.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)
titles = ['ID', 'Тип', 'Источник', 'Название в бд', 'Текст', 'Перевод']
# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Лист1')

record_fields = []
code_fields = []
id_fields = []
print(len(df1[titles[3]]))
new_list = []
for i in range(0, len(df1[titles[3]])):
    id = df1[titles[0]][i]
    id_new = id
    type = df1[titles[1]][i]
    source = df1[titles[2]][i]
    code_name = df1[titles[3]][i]
    text = df1[titles[4]][i]
    if code_name not in code_fields:
        record_fields.append([id, code_name, text])
        code_fields.append(code_name)
        id_fields.append(id)
    else:
        id_new = id_fields[code_fields.index(code_name)]
    new_list.append([id, id_new])
print(new_list)
file = open('test4.txt', 'w')
for i in new_list:
    file.write(str(i[1])+'\n')
file.close()

print(len(record_fields))
cnx = conn.connect(host='185.125.44.222', user='pwa-admin', password='}Q2yF{M;$w852}37', database='pwa', auth_plugin='mysql_native_password')
curs = cnx.cursor()
for i in record_fields:
    idd = i[0]
    code = i[1]
    ru = i[2]
    print(len(ru))
    query = "INSERT INTO `pwa`.`localization_new` (`id`,`code`,`ru`) VALUES({},'{}','{}');".format(idd, code, ru)
    curs.execute(query)
    print(query)
cnx.commit()
cnx.close()
