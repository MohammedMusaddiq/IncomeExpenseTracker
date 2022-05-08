from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.handelLogin, name="login"),
    path('signup/', views.handelSignup, name="signup"),
    path('logout/', views.handelLogout, name="logout"),
]
