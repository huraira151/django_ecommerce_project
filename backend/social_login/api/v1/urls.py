from django.urls import path
from .viewsets import *

urlpatterns = [
    path('google/', GoogleLogin.as_view()),
    path('linkedin/', LinkedinLogin.as_view()),
    path('facebook/', FacebookLogin.as_view()),
]
