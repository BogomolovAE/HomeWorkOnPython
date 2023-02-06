# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
# Модуль контроллер
# Модуль для импорта(ввода данных)
# Модуль для экспорта(вывод данных)
# Строка содержит id,имя,фамилию,номер телефона, комментрий - символ разделитель на выбор(можно использовать пробел или запятые) + файл с хранением этих строк
# *Добавить сортировку по имени или по id
# *Добавить вывод только имени и фамилии

import Import
import Export
def Main ():
    fields=["ID: ","Name: ","Surname: ","Phone number: ","Comment: "]
    command=''
    while not(command=='exit'):
        print()
        command=input('Input command, or \'help\' to print help: ').lower()
        if command=='help':
            commandList=open('Help_lesson_7.txt','r')
            for line in commandList:
                print(line)
            commandList.close()
        elif command=='add':
            Import.AddNumber(fields)
        elif command=='print_by_id':
            Export.PhonesShow(fields)
        elif command=='print_by_name':
            Export.PhonesSort(fields)    
        elif command=='print_name_only':
            Export.PhonesNameOnly(fields)           
Main()
