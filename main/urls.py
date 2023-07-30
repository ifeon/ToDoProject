from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('done/', views.task_done, name='task_done'),
    path('<int:id>/', views.task_detail, name='task_detail'),
]
