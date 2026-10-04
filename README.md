# Sprint_n

Автотесты для учебного сервиса «Доска»: https://qa-desk.education-services.ru/

## Структура проекта
Sprint_n/
constants.py — URL, эндпоинты, статус-коды, сообщения об ошибках
conftest.py — фикстуры (регистрация, объявление, очистка)
api/
user_api.py — регистрация, авторизация
listing_api.py — создание, изменение, удаление
data/
test_data.py — тестовые данные (тела объявлений, пароль, имя)
helpers/
helpers.py — генерация уникального email
assets/
listing.png — тестовая картинка для объявления
tests/
test_registration.py — регистрация
test_authorization.py — авторизация
test_create_listing.py — создание объявления
test_edit_listing.py — редактирование объявления
test_delete_listing.py — удаление объявления
requirements.txt
README.md

## Установка

```bash
pip install -r requirements.txt
```
Запуск тестов
```bash
pytest -v
```
Примечание:
Все тесты используют API-клиенты из пакета api/ и общие фикстуры из conftest.py. Тестовые данные вынесены в data/test_data.py, а генерация уникальных значений — в helpers/helpers.py