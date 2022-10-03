import csv


file_headers = ['id', 'Фамилия', 'Имя', 'Отчество', 'Кабинет', 'Должность']


def add_record(user_dict):
    global file_headers
    with open('base.csv', 'r', encoding='utf-8') as csvfile:
        index = 1
        reader = csv.DictReader(csvfile, fieldnames=file_headers)
        for row in reader:
            print(row)
            if index < int(row['id']):
                index = int(row['id'])


    with open('base.csv', 'a', encoding='utf-8') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=file_headers)
        csv_writer.writerow({'id': index + 1,
         'Фамилия': user_dict['Фамилия'],
         'Имя': user_dict['Имя'],
         'Отчество': user_dict['Отчество'],
         'Кабинет': user_dict['Кабинет'],
         'Должность': user_dict['Должность']
         })
