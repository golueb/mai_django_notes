from django.urls import path, include
from . import views
from .views import signup_view, login_view

app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<category_id>/', views.category_detail, name='detail'),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/login/', login_view, name='login'),
]