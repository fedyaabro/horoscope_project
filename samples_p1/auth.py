from datetime import datetime as dt, timedelta
import time
from samples_p1.db import list_users, query_user_last_seen


def get_email_login(attemps=3, sleep_duration=10):
    """получение логина из почты"""
    user_email = input('Введите Ваш email:\n')
    correct = False
    i = 0
    while not correct:  # пока не подходит
        i += 1
        if user_email.find('@') != -1:  # ищи @ в мейле, если нет то else
            correct = True
            user_email = user_email.split('@')[0].lower()
            # check_valid_account()
        else:
            print('Неверный e-mail, попробуйте еще раз')
            user_email = input('Введите Ваш email:\n')
            if i % attemps == 0:
                print('Слишком много попыток, подождите ' + str(sleep_duration) + ' ' + 'секунд')
                time.sleep(sleep_duration)  # таймер ожидания
    return user_email


def check_last_login():
    """Проверяем дату последнего логина и если она > 180 то просим подтвердить акк"""
    login = check_in_db()
    last_seen = query_user_last_seen(login)
    if (dt.now() - last_seen).days > 180:
        print('Вам необходимо подтвердить аккаунт')
    else:
        new_time = (dt.now() + timedelta(180)).strftime('%x')
        print('Ваш акк подтвержден до ' + new_time)


def check_in_db():
    """проверка на наличие пользователя в бд """
    known_users = []
    for users in list_users():
        known_users.append(users[0])
    login = get_email_login()
    if login in known_users:
        print('Вход выполнен', login)
    else:
        print('Вы с нами недавно, добро пожаловать', login)
    return login

# def check_valid_account():
#     """проверка валидности аккаунта"""
#     valid_date = (dt.now() + timedelta(60)).strftime('%x')
#     return print('Ваш аккаунд действителен до: ' + valid_date)
