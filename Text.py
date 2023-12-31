


main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать все контакты',
             'Добавить контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

select_menu = 'Выберите пункт меню: '

input_error = f'Ошибка ввода. Введите число от 1 до {len(main_menu) - 1}'

new_contact = {'name': 'Введите имя контакта: ', 
               'phone': 'Введите телефон: ', 
               'comment': 'Введите комментарий: '}

empty_book = 'Телефонная книга пуста или не открыта'

load_succesful = 'Телефонная книга успешно загружена'
save_succesful = 'Телефонная книга успешно сохранена'
error_load = 'Ошибка загрузки телефонной книги'
error_save = 'Ошибка сохранения телефонной книги'
print_errors= 'Ошибка изменения телефонной книги'
def add_succesful(name: str) -> str:
    return f'Контакт {name} успешно добавлен в книгу!'

exit = 'До свидания! До новыйх встреч!'

search_word = 'Введите строку для поиска: '

def empty_search(word: str) -> str:
    return f'Контакты, содержащие {word} не найдены'



def del_mess(word: str) -> str:
    return f'Контакт,{word} был удален'
