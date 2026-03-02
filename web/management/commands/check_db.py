import pymysql
from decouple import config
from django.core.management.base import BaseCommand
from pymysql.err import OperationalError


class Command(BaseCommand):
    """Проверка существования БД"""

    def handle(self, *args, **options):
        db_name = config('MYSQL_DB_NAME', cast=str)
        user = config('MYSQL_DB_USER', cast=str)
        password = config('MYSQL_DB_USER_PASSWORD', cast=str)
        host = config('MYSQL_DB_HOST', cast=str, default='localhost')
        port = config('MYSQL_DB_PORT', cast=int, default=3306)

        try:
            conn = pymysql.connect(
                database=db_name,
                user=user,
                password=password,
                host=host,
                port=port,
                charset='utf8mb4'
            )
            self.stdout.write(self.style.SUCCESS(f'БД "{db_name}" уже существует.'))
            conn.close()
        except OperationalError as e:
            self.stdout.write(self.style.WARNING(f'Ошибка MySQL. Код: {e.args[0]}. Сообщение: {e.args[1]}'))
