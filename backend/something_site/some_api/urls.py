from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('extract_lotto_number/', views.GetListApi.as_view()),
]
