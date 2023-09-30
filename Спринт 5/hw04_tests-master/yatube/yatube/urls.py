from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #  регистрация и авторизация
    path("auth/", include("users.urls")),

    #  если нужного шаблона для /auth не нашлось в файле users.urls —
    #  ищем совпадения в файле django.contrib.auth.urls
    path("auth/", include("django.contrib.auth.urls")),

    #  раздел администратора
    path("admin/", admin.site.urls),

    #  обработчик для главной страницы ищем в urls.py приложения posts
    path("", include("posts.urls")),
    path('about/', include('about.urls', namespace='about')),
]
handler404 = "posts.views.page_not_found"  # noqa
handler500 = "posts.views.server_error"  # noqa
