from django.urls import path

from . import views

urlpatterns = [
    path('', views.allavis, name="allavis"),
    path('<int:blog_id>/', views.detail, name='detail'),
]
