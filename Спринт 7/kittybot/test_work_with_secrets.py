# test_work_with_secrets.py

import os

from dotenv import load_dotenv

load_dotenv()
# Теперь переменная TOKEN, описанная в файле .env,
# доступна в пространстве переменных окружения

secret_token = os.getenv('TOKEN')
