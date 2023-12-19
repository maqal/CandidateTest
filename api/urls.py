from django.urls import path
from .views import *

urlpatterns = [
    path('member', MemberList.as_view()),
    path("member/<str:pk>", MemberDetails.as_view()),
]