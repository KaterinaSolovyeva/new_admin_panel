## Как запустить проект:
Создайте env и envdsn файлы в той же директории, где описаны их example файлы

Запустите docker-compose командой:
```
docker-compose up -d
```
Создайте миграции и соберите статику командой:
```
make setup
```
Загрузите первоначальные данные из sqlite в postgres командой (не забудьте заполнить .envdsn файл в папке django_api/sqlite_to_postgres). После этого сработает сервис ETL на загрузку в ElasticSearch:
```
make load_data
```
Создайте суперпользователя Django:
```
make admin
```
Команда для подключения к серверу redis:
```
make redis
```
## Запуск в браузере
- Полнотекстовый поиск по фильмам - http://127.0.0.1:9200/movies/_search
- Открытие административного сайта - http://127.0.0.1:80/admin/
- Django Api - http://127.0.0.1:80/api/v1/movies/
