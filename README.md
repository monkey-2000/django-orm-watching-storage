# django-orm-watching-storage

[Учебный сайт "Пульт охраны банка", написанный в рамках курса "Знакомство с Django: ORM" [dvmn.org](dvmn.org). Реализован вывод информации из базы данных банка:
- об активных пропусках (имя владельца, код пропуска, дата регистрации);
- о всех посещениях хранилища для каждого активного пропуска (дата посещения, продолжительность визита, был ли визит продолжительным);
- о сотрудниках, находящихся в хранилище сейчас (имя владельцаб код пропуска, дата регистрации).]

### Как установить
[Скачать файлы проекта.В директории проекта создать файл .env с переменными:
DEFAULT_HOST
DEFAULT_PORT
DEFAULT_NAME
DEFAULT_USER
DEFAULT_PASSWORD
SECRET_KEY
Для работы сайта необходимо задать значения, позволяющие получить доступ к базе данных (см. на сайте [dvmn.org](dvmn.org)). 
Также в файле .env указать режим отладки DEBUG=true/false]

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
