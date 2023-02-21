from os import path 
import re
file_base = "base.txt" 
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass
def read_records():
   global all_data, id
   with open(file_base,"r",encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
           id = int(len(all_data))
        return all_data

def show_all():
    if not all_data:
       print("Empty data")
    else:
       print(*all_data, sep="\n")

def add_new_contact():
    global id
    array = ['surname','name','surname_2','phone_number']
    string = ''
    id += 1
    for  i in array:
        string += input("\033[32m{}".format(f"enter {i} ")) + " "
    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f'{id} {string}\n')

def sear_a_record():
    global file_base
    print("\033[33m{}".format("Режим поиска контакта, введите Фамилию Имя или Отчество"))
    search_string = input("\n")
    with open(file_base,"r", encoding="utf-8") as f:
        for i in f:
            if search_string in i:
                print(i.strip())
    return i

def rewrite(line):
    global id
    # id-=1
    with open(file_base,"w", encoding="utf-8") as f:
        for item in line:
            f.write(("%s\n" % item).strip()+"\n")

def delete_contact():
    global file_base
    show_all()
    line = []
    print("Выберите контакт для удаления:")
    id = str(input("Введите ID контакта\n"))
    with open(file_base,"r", encoding="utf-8") as f:
        for i in f:
            if i[0:1] !=id:
                line+=[i]
        print(line)
    return line


# функция подсчета количества контактов
def count_line():
    return len(re.findall(r"[\n']+", open('base.txt').read()))


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("\033[34m{}".format("Phone book:\n"
                    "1. Show all records\n"
                    "2. Add a record\n"
                    "3. Search a record\n"
                    "4. Delete\n"
                    "5. Exit\n"))
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                sear_a_record()
            case "4":
                rewrite(delete_contact())
            case "5":
                play = False
            case _:
                print("Try again!\n")
main_menu()