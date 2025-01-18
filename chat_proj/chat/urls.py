from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Default home route
    path('chat/<str:username>/', views.chat_view, name='chat'),
]

from django.contrib.auth.views import LoginView

urlpatterns += [
    path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),
]

from django.contrib.auth.views import LogoutView

urlpatterns += [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

urlpatterns += [
    path('signup/', views.signup_view, name='signup'),
]

