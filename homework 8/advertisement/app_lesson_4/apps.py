from django.apps import AppConfig


class AppLesson4Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_lesson_4'
    #если ввожу русское слово то выходит ошибка
    verbose_name = ('ads')
