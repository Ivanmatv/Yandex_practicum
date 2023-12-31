# api_final

### Описание: 
Это API позволяте работать любому мобильному устройству с сайтом Yatube через приложение или чат-бот; через него же можно будет передавать данные по запросу публикаций: со всего сайта, определённой публикации по id, удаления публикации её автором, комментария к этой публикации и удаления её автором; добавление новой публикации в коллекцию публикаций; обновление публикации по id, обновить публикацию может только автор публикации; добавление нового комментария к статье;
получение списка доступных сообществ, получение информации о сообществе по id; возвращение всех подписок пользователя, сделавшего запрос, так же подписка на других пользователей; получение JWT-токена и его обновление, и проверка.

### Установка:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Ivanmatv/api_final_yatube.git
```

```
cd kittygram_backend
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры:
Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube. В документации описано, как должен работать ваш API. Документация представлена в формате Redoc.
