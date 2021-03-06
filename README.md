# django-orm-watching-storage

Учебный сайт "Пульт охраны банка", написанный в рамках курса "Знакомство с Django: ORM" [dvmn.org](dvmn.org). Реализован вывод информации из базы данных банка:
- об активных пропусках (имя владельца, код пропуска, дата регистрации);
- о всех посещениях хранилища для каждого активного пропуска (дата посещения, продолжительность визита, был ли визит продолжительным);
- о сотрудниках, находящихся в хранилище сейчас (имя владельца, код пропуска, дата регистрации).

Для работы сайта необходим доступ к учебной базе данных. Параметры доступа указаны в соответствующем уроке на сайте [dvmn.org](dvmn.org)

### Как установить

Скачайте файлы проекта. Заполните все поля переменной 
```DB_URL='postgres://USER:PASSWORD@HOST:PORT/NAME'``` в файле env_template. 
Измените название файла env_template на .env.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Пример запуска скрипта

Cайт можно запустить на локальном сервере (localhost) командой:```python manage.py runserver 0.0.0.0:8000```
В случае удачного выполнения команды в терминале будет выведено следующее сообщение:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
[current date nad time]
Django version 3.2.12, using settings 'project.settings'
Starting development server at http://[localhost]:8000/
Quit the server with CONTROL-C.
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
