from django.contrib import admin
from django.urls import path
from translate_web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='home')
]
