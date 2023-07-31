from django.contrib import admin
from django.urls import path
from balance.views import TestView, UsersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TestView.as_view()),
    path('api/balances/', UsersView.as_view()),

]
