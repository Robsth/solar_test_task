## Test task by RTK-Solar

Реализовать Django приложение, позволяющее добавлять сайты (пары название/адрес), и производить их мониторинг в автоматическом режиме. Предполагается, что раз в некоторое время (настраивается в настройках приложения) происходит опрос каждого сайта, после чего, в зависимости от результата ответа сайту устанавливается соответствующий статус. Список сайтов, дату последнего опроса и статус должна быть возможность просматривать в панели администрирования.

Реализовать REST API с возможностью получить список всех сайтов с их данными и фильтрацией по статусу (рабочие/нерабочие). Возможность создавать/редактировать данные через API не предполагается.

Будет плюсом: ограничение на доступ к API только для залогиненного пользователя. Для всех остальных должен возвращаться пустой список.

### Main tools:

- Python 3
- Django 3
- Django REST Framework
- Docker / Docker-compose
- Redis
- Celery
- Postgresql

### API Endpoints

- `127.0.0.1:8000/admin/` - django admin
- `127.0.0.1:8000/api/sites/` - list of sites (DRF view)
- `127.0.0.1:8000/api/sites/[?status=available | unavailable]` - status filter

### Instructions

Clone the repository and:
```sh
$ docker-compose up --build
```

To create a user you should open a new terminal and:
```sh
$ docker-compose exec backend bash
$ python manage.py createsuperuser
```

