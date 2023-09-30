from pyrogram import Client

api_id = 22836206
api_hash = 'a5d0cc87903e5515e755490c8de5f068'

# Создаём программный клиент, передаём в него
# имя сессии и данные для аутентификации в Client API
app = Client('my_account', api_id, api_hash)

app.start()
# Отправляем сообщение
# Первый параметр - это id чата или имя получателя.
# Зарезервированное слово 'me' означает собственный аккаунт отправителя.
app.send_message('me', 'Привет, это я!')
app.stop()
