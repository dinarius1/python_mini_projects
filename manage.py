"CRUD"
# create - создать
# read - читать
# update - обновлять
# delete - удаление

from products import create, read  #по названию файла ищет нужный файл

while True:
    oper = input('c/r/d/u: ')
    if oper == 'c':
        create()
    elif oper == 'r':
        read()
