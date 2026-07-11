# QA Portfolio

Практическое портфолио по мануальному тестированию — pet-проект для отработки навыков QA.

## Что внутри

### 🔹 Login Form Testing
Тестирование формы логина на [saucedemo.com](https://www.saucedemo.com) — 11 тест-кейсов (позитивные/негативные сценарии, граничные значения, спецсимволы, регистр) и 1 баг-репорт.

📁 [`login-form-testing/`](./login-form-testing)

### 🔹 API Testing
Тестирование публичного REST API [reqres.in](https://reqres.in) в Postman — 10 запросов (GET, POST, PUT, PATCH, DELETE), включая проверку кодов ответа, валидации данных и найденные несоответствия.

📁 [`api-testing/`](./api-testing)

## Ключевые находки
- Обнаружено, что mock-API reqres.in не выполняет валидацию входных данных и существования ресурсов (POST с пустым телом, PATCH/DELETE несуществующего пользователя всё равно возвращают успешный статус)
- Найден баг: отсутствие ограничения длины ввода в полях username/password на saucedemo.com

## Инструменты
Postman, Chrome DevTools, Markdown
