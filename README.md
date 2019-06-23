# django-boilerplate

## Внешние зависимости
- docker 
- docker-compose
- python3.7
- pip3
- pipenv

## Задачи
- [ ] добавить поддержку внешней базы данных
- [ ] сделать fuzzy counter для ускорения получения кол-ва записей в пагинации

## Кейсы
- [ ] Полнотекстовый поиск PostgreSQL
- [ ] rest api
- [ ] jsonrpc api
- [ ] Авторизация соц.сетей
- [ ] Парсинг xml, html
- [ ] Экспорт/импорт xlsx, csv
- [ ] Тестирование api, поведения, юнит тесты, mock, покрытие кода
- [ ] Авторизация с помощью jwt
- [ ] Фильтрация, поиск, пагинация таблицы
- [ ] Websocket + jsonrpc + elm чат.

## Функции проекта
- [x] docker-compose - сборка проекта в контейнеры
- [x] celery - очереди задач (периодические и отложенные задачи)
- [x] redis - кэ, брокер сообщений
- [x] nginx - фронетенд сервер (статика, медиа, прокси запросов на бекенд)
- [x] cherrypy + django (backend сервер)
- [x] postgres - реляционная база данных
- [x] supervisor - управление процессами
- [x] sentry - логгирование ошибок во внешнем сервисе
- [x] logger - пример проекта
- [x] pipenv - пакетный менеджер
- [x] flake8 - проверка форматирования
- [x] .gitignore - игнорирование временных файлов и секретов
- [x] .env - секреты передаются читаются из файла как переменные окружения
- [x] debug_toolbar - дебаггинг sql запросов и не только

## Функций в приложении logger 
- [x] Management command с прогрессбаром
- [x] Фронтенд пагинация, поиск
- [x] Количество уникальных IP
- [x] Top 10 самых распространенных IP адресов, в формате таблички где указан IP адрес и количество его вхождений
- [x] Количество GET, POST, ... (http методов)
- [x] Общее кол-во переданных байт (суммарное значение по полю "размер ответа")
- [x] Хорошее оформление и комментирование кода (не излишнее, но хорошее);
- [x] Оформление frontend части;
- [x] Упаковка проекта в docker/docker-compose;
- [x] Оптимизация запросов к БД;
- [x] Кнопка экспорта данных на таблице с результатами, при нажатии на которую будет скачиваться файлик в формате XLSX с результатами выдачи;

## Запуск с помощью docker-compose
### Переменные окружения (Шаг 1)
```
cp conf/.env-example conf/.env
cp devops/.env-example devops/.env
```

### Запуск контейнеров (Шаг 2)
```
cd devops && docker-compose -p django-boilerplate up
```

## Запуск сервера разработки 
### Переменные окружения (Шаг 1)
```
cp conf/.env-example conf/.env
cp devops/.env-example devops/.env
```

Заменить переменные в conf/.env
```
POSTGRES_DB_HOST=localhost
POSTGRES_DB_PORT=54321
```

### Виртуальное окружение и зависимости (Шаг 2)
```
pipenv shell --python python3.7
pipenv install # in virtualenv
```

### Запуск postgres (Шаг 3)
```
cd devops && docker-compose -p django-boilerplate up postgres
```

### Запуск сервера (Шаг 4)
```
python manage.py runserver
```

## Подключиться к контейнеру приложения
```
docker exec -it django-boilerplate_app_1 sh
```

## Запустить скрипт загрузки логов 
```
python manage.py download -su http://www.almhuette-raith.at/apache-log/access.log
```

## Фикстуры
```
python manage.py dumpdata logger.log > apps/logger/fixtures/log.json 
python manage.py loaddata apps/logger/fixtures/log.json
```
