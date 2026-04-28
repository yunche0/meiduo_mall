from django.urls import path
from apps.users.views import UsernamecountView
urlpatterns = [
    path('usernames/<username>/count/',UsernamecountView.as_view()),
]