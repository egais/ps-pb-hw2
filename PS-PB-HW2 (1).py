# Создаем словари для аккаунтов
account1 = {'login': 'ivan' , 'password': 'q1'}
account2 = {'login': 'petr' , 'password': 'q2'}
account3 = {'login': 'olga' , 'password': 'q3'}
account4 = {'login': 'anna' , 'password': 'q4'}

# Создаем словари для юзеров
user1 = {'name': 'Иван', 'age': '20', 'account':account1}
user2 = {'name': 'Петр', 'age': '25', 'account':account2}
user3 = {'name': 'Ольга', 'age': '18', 'account':account3}
user4 = {'name': 'Анна', 'age': '27', 'account':account4}

# Создаем список словарей для юзера

user_list = [user1, user2, user3, user4, ]

# Вводим значение ключа и передаем значение ключа на user_key
#  методом lower() приводим к нижнему регистру

user_key = input('введите ключ (name или account):').lower()
print(user_key)
try:
    print(f'значение ключа {user_key} name для юзера = {user1[user_key]}')
    print(f'значение ключа {user_key} name для юзера = {user2[user_key]}')
    print(f'значение ключа {user_key} name для юзера = {user3[user_key]}')
    print(f'значение ключа {user_key} name для юзера = {user4[user_key]}')
except KeyError:
    print('введенный ключ не найден')
user_number = input('введите порядковый номер: ')
user = user_list[int(user_number)-1]
try:
    print(f"данные по юзеру № {user_number}")
    print(f"имя: {user['name']}")
    print(f"возраст: {user['age']}")
    print(f"логин: {user['account']['login']}")
    print(f"пароль: {user['account']['password']}")
except TypeError:
    print('Пользователь с указанным номером не найден.')
# Высчитываем средний возраст всех юзеров
age_user1 = 20
age_user2 = 25
age_user3 = 18
age_user4 = 27
m_age1 = (age_user1 + age_user2 + age_user3 + age_user4) / len(user_list)
print('Средний возраст пользователей:' + str(m_age1))

user_end = input('Введите номер пользователя, которого нужно переместить в конец:')
new_user = user_list.pop(int(user_end)-1)
print(user_list)
user_list.append(new_user)
print(user_list)

