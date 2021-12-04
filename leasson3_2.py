# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def person_profile(**kwargs):
    return f"Имя: {kwargs['name']}, Фамилия: {kwargs['surname']}, Год рождения: {kwargs['birth_year']}, " \
           f"Город проживания: {kwargs['city']}, Почта: {kwargs['email']}, Телефон: {kwargs['phone']} "


print(person_profile(name="Dmitry", surname="Churilov", birth_year="1995", city="Saint-P",
                     email="churilov.dmitrycd@mail.ru", phone="88005553535"))
