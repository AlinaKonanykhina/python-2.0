def get_choice():
    return int(input('Добро пожаловать в справочник ООО "Питон"\n Введите номер операции: 1-добавить: 2-поиск:'))

def get_element():
    return input('Введите фамилию для поиска - ')


def get_dict():
    keys = ['Фамилия', 'Имя', 'Отчество', 'Кабинет', 'Должность', ]
    user_dict = {}
    for i in range(5):
        user_dict[keys[i]] = input(f'Введите {keys[i]} - ')
    return user_dict
    print(user_dict)



def get_result():
    print('успех')
    pass
