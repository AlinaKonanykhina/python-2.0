import csv


file_headers = ['id', 'Фамилия', 'Имя', 'Отчество', 'Кабинет', 'Должность']


def get_search(user_dict):
    with open('base.csv', 'r', encoding='utf-8') as csvfile:
        index = 1
        reader = csv.DictReader(csvfile, fieldnames=file_headers)
        for key in reader:
            print(key)





# for k in user_dict:                                    #.items():
#    if к['Должность'] == 'Должность':
#        print(k['Фамилия'])
#        return k
