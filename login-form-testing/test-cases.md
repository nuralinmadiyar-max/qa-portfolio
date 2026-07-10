# Тест-кейсы: Форма логина (saucedemo.com)

| № | Предусловие | Шаги | Ожидаемый результат | Фактический результат | Статус |
|---|---|---|---|---|---|
| 1 | Пользователь на странице логина | 1) Оставить username пустым 2) Оставить password пустым 3) Нажать Login | Ошибка, вход не выполняется | `Epic sadface: Username is required` | Passed |
| 2 | Пользователь на странице логина | 1) Ввести валидный username 2) Оставить password пустым 3) Нажать Login | Ошибка, вход не выполняется | `Epic sadface: Password is required` | Passed |
| 3 | Пользователь на странице логина | 1) Ввести невалидный username 2) Ввести невалидный password 3) Нажать Login | Ошибка, вход не выполняется | `Epic sadface: Username and password do not match any user in this service` | Passed |
| 4 | Пользователь на странице логина | 1) Ввести username `standard_user` 2) Ввести password `secret_sauce` 3) Нажать Login | Успешный вход, переход на страницу каталога | Успешный вход выполнен | Passed |
| 5 | Пользователь на странице логина | 1) Ввести username `locked_out_user` 2) Ввести password `secret_sauce` 3) Нажать Login | Вход не выполняется, сообщение о блокировке | `Epic sadface: Sorry, this user has been locked out.` | Passed |
| 6 | Пользователь на странице логина | 1) Ввести username `#@` 2) Ввести password `#@` 3) Нажать Login | Вход не выполняется (пользователя не существует) | `Epic sadface: Username and password do not match any user in this service` | Passed |
| 7 | Пользователь на странице логина | 1) Ввести username `!"` 2) Ввести password `!"` 3) Нажать Login | Вход не выполняется (пользователя не существует) | `Epic sadface: Username and password do not match any user in this service` | Passed |
| 8 | Пользователь на странице логина | 1) Ввести username `№;` 2) Ввести password `№;` 3) Нажать Login | Вход не выполняется (пользователя не существует) | `Epic sadface: Username and password do not match any user in this service` | Passed |
| 9 | Пользователь на странице логина | 1) Ввести username `Standard_user` (с заглавной буквы) 2) Ввести password `Secret_sauce` 3) Нажать Login | Вход не выполняется — система регистрозависима | `Epic sadface: Username and password do not match any user in this service` | Passed |
| 10 | Пользователь на странице логина | 1) Ввести username из 300+ символов 2) Ввести валидный password 3) Нажать Login | Поле должно иметь ограничение длины ввода | Поле не ограничивает длину ввода, ошибка при Login | Passed (см. баг-репорт #1) |
| 11 | Пользователь на странице логина | 1) Ввести username `standard _ user` (с пробелами) 2) Ввести password `secret_sauce` 3) Нажать Login | Вход не выполняется (username невалиден) | `Epic sadface: Username and password do not match any user in this service` | Passed |
