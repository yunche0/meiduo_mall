from django.urls import path
from apps.users.views import UsernamecountView,RegisterView
urlpatterns = [
    path('usernames/<username:username>/count/',UsernamecountView.as_view()),
    path('register/',RegisterView.as_view()),

]