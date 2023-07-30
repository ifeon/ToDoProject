from django.contrib import admin
from django.urls import path, include
from main import views
from main.views import RegView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='home'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/registration/', RegView.as_view(), name='registration'),
    path('profile/', include('main.urls', namespace='main')),
]
