from django.urls import path
from apps.users.views import UsernamecountView,RegisterView,LoginView
urlpatterns = [
    path('usernames/<username:username>/count/',UsernamecountView.as_view()),
    path('register/',RegisterView.as_view()),

    path('login/',LoginView.as_view()),
]