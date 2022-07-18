from django.urls import path
from . import views

urlpatterns = [

    path('', views.listStudent, name = 'list'),
    path('register/', views.studentRegister , name = 'register'),
    path('edit/<str:pk>/', views.editStudent, name='edit'),
    path('delete/<str:pk>/', views.deleteStudent, name='delete'),
    path('show/<str:pk>/', views.studentView, name='show'),
]