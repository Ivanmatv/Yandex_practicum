# api_yamdb
![yamdb_workflow](https://github.com/Ivanmatv/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

### Опиание проекта.
Cайт Foodgram - «Продуктовый помощник». На этом сервисе пользователи смогут публиковать рецепты блюд, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Создайте файл .env
Пример:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<ключ в одинарных ковычках>
```

### Установка:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Ivanmatv/foodgram-project-react.git
```
```
cd foodgram-project-react
```
Клонировать и установить виртуальное окружение:

- для MacOS
```
python3 -m venv venv
```
- для Windows
```
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```
Установить зависимости:

```
cd backend
```
```
pip install -r requirements.txt
```

Применить миграции:
```
python manage.py makemigrations users
```
```
python manage.py makemigrations recipes
```

```
python manage.py migrate
```

***- В папке с файлом manage.py выполните команду для запуска локально:***

```
python manage.py runserver
```

Запустить все контейнера командой:
```
cd infra
```
```
docker-compose up -d --build
```

Выполнить миграции:

``` 
docker-compose exec backend python manage.py migrate 
```

Создайте суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```

Загружаем статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input 
```

Наполните базу данных ингредиентами и тегами. Выполняйте команду из дериктории где находится файл manage.py:
```
python manage.py load_csv_data

```

Остановить работу всех контейнеров командой:
```
docker-compose down
```

### Примеры:
Когда вы запустите проект, по адресу  http://localhost/api/docs/ будет доступна документация для API foodgram-project-react. В документации описано, как должен работать ваш API. Документация представлена в формате Redoc.

В проекте доступны следующие эндпоинты: 
http://51.250.15.168/api/recipes/ - Получение рецепта

{
    "count": 123,
    "next": "http://foodgram.example.org/api/recipes/?page=4",
    "previous": "http://foodgram.example.org/api/recipes/?page=2",
  - "results": [
    + { ... }
    ]
}

http://51.250.15.168/api/users/ - Получение списка пользователей

http://51.250.15.168/api/auth/token/login/ - Получение токена авторизации

http://51.250.15.168/api/auth/token/login/ - Получение списка тегов

http://51.250.15.168/api/recipes/download_shopping_cart/ - Скачать список покупок

http://51.250.15.168/api/recipes/{id}/favorite/ - Добавить рецепт в избранное 

http://51.250.15.168/api/users/subscriptions/ - Получение списка подписок

http://51.250.15.168/api/users/subscriptions/ - Получение списка ингредиента 

### Использумые технологии:

- Python
- Django
- PyJWT
- Django Rest Framework
- Docker
- Nginx
- Rest API

### Авторы проекта:

https://github.com/Ivanmatv - Иван Матвеев

админка
Адрес электронной почты: ivan@gmail.com
пароль matveev1