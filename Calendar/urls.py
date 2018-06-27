from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('appointments/', include('appointments.urls')),
    # path('appointments/', include('django.contrib.auth.urls')),
    path('login', auth_view.login, name = 'login' ),
    path('logout', auth_view.logout, name = 'logout'),

]
