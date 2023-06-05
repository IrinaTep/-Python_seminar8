# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.

# # ТЕОРИЯ

# # w - перезапись
# # r - чтение
# # a - дозапись
# # r+ - чтение + запись
# # b - байт

# # open - функция, которая создает некого менеджера работы с файлом; нужно задать путь (как правило указывают отдельной переменной) и режим
# # open(r"data\new.txt", "w") # в python \ обозначает переход на новую строку, можно экранироать (поставить обратный слэш), но удобнее поставить (сырую) букву r
# FILE_PATH = r'new.txt'

# # open(FILE_PATH, 'w')

# # путь может задаваться через библиотеку
# # import pathlib

# # f = open(FILE_PATH, 'w')
# # f.write('cvbnm') # w создает именно папку, файл создать не сможет!; в режиме w полностью удалит предыдущее и перезапишет
# # f.close
# # with - менеджер для работы с файлом, с которым не нужно закрывать файлы в ручную
# # with open(FILE_PATH, 'w') as f: # в случае ошибки этот менеджер сам корректно закроет файл
# #     f.write('Hello, World!')
# with open(FILE_PATH, 'a') as f: # дописывает с последнего символа Hello, World!Hello, World!
#     # f.write('Hello, World!')
# # чтобы добавить запись с новой строки, нужно поставить обратный слэш n
#     f.write('\nHello, World!')
# # read может забить оперативную память, если файл большой; этот менеджер практически не используется
# # with open(FILE_PATH, 'r') as f:  
# #     print(f.read()) # в скобках передаем, сколько символов он должен прочитать; если ничего не передаем, то прочитает весь файл

# # with open(FILE_PATH, 'r') as f:  
# #     # print(f.readline())
# #     # print(f.readline())
# #     print(f.readlines()) # readlines считает все строки с невидимыми символами в качестве списка ['Hello, World!Hello, World!\n', 'Hello, World!']
# #     # print(f.readlines()[0].strip()) # strip убирает все переходы, пробелы и т. д. так можно обработать каждую строку

# # Самый предпочтительный вариант чтения:
# with open(FILE_PATH, 'r') as f:
#     for line in f:
#         print(line.strip())



# # РЕШЕНИЕ ЗАДАЧИ НА СЕМИНАРЕ
# import os
# import shutil
# os.chdir('C:\\Users\\andre\\Desktop\\Ирина\\GEEKBRAINS\\Знакомство_с_Python\\Семинар_8')
# print(os.getcwd())

# # with open('Телефонный_справочник.txt', 'w') as f:
# #     f.write('Ivanov,Ivan,+123 ')
# #     f.write('\nPetrov,Petr,+456 ')
# #     f.write('\nSemyonov,Semyon,+789 ')
# def add_user():
#     with open('Телефонный_справочник.txt', 'a') as f:
#         f.write('\n')
#         f.write(input('Введите Фамилию,Имя,Телефон: '))

# def read_all_users():
#     with open('Телефонный_справочник.txt', 'r') as f:
#         for line in f:
#             print(line.strip())

# def search_user():
#     with open('Телефонный_справочник.txt', 'r') as f:
#         search = input("Что ищем? - ")
#         for line in f:
#             if search in line:
#                 print(line.strip())
#             # else:
#             #     print("Таких нет")

# # with open('Телефонный_справочник.txt', 'r') as f:
# #     for line in f:
# #         print(type(line))

# def info_func():
#     print("\n1. Показать весь справочник ")
#     print("2. Добавить пользователя ")
#     print("3. Поиск пользователя ")
#     print("4. Выход")

# info_func()
# # user_action = int(input("Выберите функцию через цифру - "))
# while (user_action := int(input("Выберите функцию через цифру - "))) != 4:
#     match user_action:
#         case 1: 
#             read_all_users()
#             info_func()
#         case 2:
#             add_user()
#             info_func()
#         case 3:
#             search_user()
#             info_func()
#         case 4:
#             break
#         case _:
#             print("Нет такой функции")

 
# match subject:
#     case <pattern_1>:
#         <action_1>
#     case <pattern_2>:
#         <action_2>
#     case <pattern_3>:
#         <action_3>
#     case_:
#         <action_wildcard>

# ДОМАШНЕЕ ЗАДАНИЕ
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

import os
os.chdir('C:\\Users\\andre\\Desktop\\Ирина\\GEEKBRAINS\\Знакомство_с_Python\\Семинар_8')
print(os.getcwd())

def add_user():
    with open('Телефонный_справочник.txt', 'a') as f:
        f.write('\n')
        f.write(input('Введите Фамилию,Имя,Телефон: '))

def read_all_users():
    with open('Телефонный_справочник.txt', 'r') as f:
        for line in f:
            print(line.strip())

def search_user():
    with open('Телефонный_справочник.txt', 'r') as f:
        search = input("Что ищем? - ")
        found_users = []
        for line in f:
            if search in line:
                found_users.append(line.strip())
        if found_users:
            print("Результаты поиска:")
            for user in found_users:
                print(user)
        else:
            print("Пользователь не найден.")

def update_user():
    search = input("Введите имя или фамилию пользователя для изменения: ")
    temp_file = 'temp.txt'
    found = False
    with open('Телефонный_справочник.txt', 'r') as f, open(temp_file, 'w') as temp:
        for line in f:
            if search in line:
                print(line)
                new_data = input("Введите новые данные в формате Фамилия,Имя,Телефон: ")
                if len(new_data) > 0:
                    temp.write(new_data + '\n')
                    found = True
                else:
                    temp.write(line)
            else:
                temp.write(line)
    if found:
        os.remove('Телефонный_справочник.txt')
        os.rename(temp_file, 'Телефонный_справочник.txt')
        print("Данные пользователя изменены.")
    else:
        os.remove(temp_file)
        print("Пользователь не найден.")

def delete_user():
    search = input("Введите имя или фамилию пользователя для удаления: ")
    temp_file = 'temp.txt'
    deleted = False
    with open('Телефонный_справочник.txt', 'r') as f, open(temp_file, 'w') as temp:
        for line in f:
            if search not in line:
                temp.write(line)
            else:
                deleted = True
    if deleted:
        os.remove('Телефонный_справочник.txt')
        os.rename(temp_file, 'Телефонный_справочник.txt')
        print("Пользователь удален.")
    else:
        os.remove(temp_file)
        print("Пользователь не найден.")

def info_func():
    print("\n1. Показать весь справочник ")
    print("2. Добавить пользователя ")
    print("3. Поиск пользователя ")
    print("4. Изменить данные пользователя ")
    print("5. Удалить пользователя ")
    print("6. Выход")

info_func()
while (user_action := int(input("Выберите функцию через цифру - "))) != 6:
    match user_action:
        case 1:
            read_all_users()
        case 2:
            add_user()
        case 3:
            search_user()
        case 4:
            update_user()            
        case 5:
            delete_user()            
        case 6:
            break
        case _:
            print("Нет такого пункта меню")
    info_func()