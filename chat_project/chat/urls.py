from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('<int:user_id>/', views.chat_messages, name='chat_messages'),
    path('accounts/signup/', views.signup_view, name='signup'),
  # Add signup route
]
