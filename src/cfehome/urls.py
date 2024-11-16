from django.contrib import admin
from django.urls import path, include
from auth import views as auth_views
from .views import home_page_view

urlpatterns = [
    path('', home_page_view, name='home'),
    path("hello-world/", home_page_view),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register_view, name='register'),
    path('accounts/', include('allauth.urls')),
]
