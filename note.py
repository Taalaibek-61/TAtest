#Напишите проект, содержащий функционал работы с заметками. 
#Программа должна уметь создавать заметку, сохранять её, читать список заметок, 
#редактировать заметку, удалять заметку.



import os
def add_notes():
    name = input('Введите название заметки: ')          
    content = input('Введите содержание или текст заметки: ')   
    data = open('C:\\Users\User\\Searches\\Desktop\\Python_2\\test_1\\books.txt' ,'a', encoding='utf-8')
    data.writelines([  name, ' ',  content, ' ' '\n']) 
    data.close()

def print_data():
    with open('C:\\Users\User\\Searches\\Desktop\\Python_2\\test_1\\books.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def search():
    search_name = input('Введите название заметки: ')
    with open('C:\\Users\User\\Searches\\Desktop\\Python_2\\test_1\\books.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)

                 
def del_notes():
    del_name = input('Введите название заметки, которую хотите удалить: ')
    with open('C:\\Users\User\\Searches\\Desktop\\Python_2\\test_1\\books.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
        for i_line in range(len(d)):
            if del_name in d[i_line]:
                del d[i_line]
    with open('C:\\Users\User\\Searches\\Desktop\\Python_2\\test_1\\books.txt', 'w', encoding='utf-8') as data:
        print(d)
        for line in d:
            data.write(line)

def change_notes():
    change_name = input('Введите название заметки, которую хотите изменить: ')
    
    name = input('Введите новое название: ')
    content = input('Введите новое содержание или текст заметки: ')
   

    with open('C:\\Users\User\\Searches\\Desktop\\Python_2\\test_1\\books.txt', 'r',encoding='utf-8') as data:
        d = data.readlines()
    for i_line in range(len(d)):
        if change_name in d[i_line]:
            d[i_line] =  name +' ' +  content + ' ''\n'

    with open('C:\\Users\User\\Searches\\Desktop\\Python_2\\test_1\\books.txt', 'r',encoding='utf-8') as data:
        for line in d:
            data.write(line)
def ui():
    os.system('cls')
    print('''1 - добавить заметку
2 - поиск
3 - вывод в консоль
4 - удалить заметку
5 - изменить заметку
6- выход''')
    user_input = input('Введите нужный вариант: ')
    while user_input != '6':
        if user_input == '1':
            add_notes()
        elif user_input == '2':
            search()
        elif user_input == '3':
            print_data()
        elif user_input == '4':
            del_notes()
        elif user_input == '5':
            change_notes()

        else:
            print('Вы ввели некорректные данные попробуйте еще раз')
        user_input = input('Введите нужный вариант: ')
        os.system('cls')
        print('''1 - добавить заметку
2 - поиск
3 - вывод в консоль
4 - удалить заметку
5 - изменить заметку
6 - выход''')

def main():
    ui()

if __name__ == "__main__":
    main