# QRKot - Фонд поддержки котиков 🐱💕

Веб-приложение для сбора пожертвований на целевые проекты помощи кошкам. 
От покупки корма до строительства приютов — каждый может помочь!

## ✨ Особенности

- **Проекты помощи** - Создавайте и управляйте целевыми сборами
- **Пожертвования** - Поддерживайте проекты любой суммой
- **Автоматическое распределение** - Система сама распределяет средства между проектами
- **Супер-администрирование** - Расширенные возможности для управляющих фондом

## 🚀 Технологии

- Python 3.10+
- FastAPI (веб-фреймворк)
- SQLAlchemy (ORM)
- Alembic (миграции БД)
- SQLite (база данных)
- Uvicorn (ASGI-сервер)
- Pydantic (валидация данных)

## 📦 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/IgorMogilin/cat_charity_fund.git
cd qrkot
```

2. Создайте и активируйте виртуальное окружение:
``` bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Настройте базу данных:
```bash
alembic upgrade head
```

5. Запустите приложение:
```bash
uvicorn app.main:app --reload
```

## 📚 Документация API

После запуска приложения документация доступна по адресам:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔐 Аутентификация

Система использует JWT-токены. Для получения токена:

```bash
curl -X POST "http://localhost:8000/auth/jwt/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin@example.com&password=secret"
```

Пример использования токена:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8000/donations/my
```

## Автор

- [Могилин Игорь](https://github.com/IgorMogilin)