# Интерактивная карта города с интересными местами, их фото и описанием.
![](static/ezgif.com-gif-maker_4nWhtfQ.gif)
Пример работы [сайта](http://kmorales.pythonanywhere.com).

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```
pip install -r requirements.txt
```

Создайте базу данных SQLite

```
python3 manage.py migrate
```

Запустите разработческий сервер

```
python3 manage.py runserver
```

Для перехода на сайт перейдите по ссылке [http://127.0.0.1:8000](http://127.0.0.1:8000)

Для внесения изменений в базу данных создайте суперпользователя:

```
python3 manage.py createsuperuser
```

и перейдите в админку [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Добавлять новые точки на карте можно вводя данные через админку.

Так же вы можете добавить файлы `json` [с такой структурой](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе%20Bizone.json) в папку `static/places/` и запустить команду:

```
python3 manage.py load_place
```

В результате выполнения база данных пополнится новыми местами.

## Переменные окружения

- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).
