from django.urls import path
from . import views

urlpatterns = [
    path('replies/', views.ReplyList.as_view()),
    path('replies/<int:pk>/', views.ReplyDetail.as_view()),
]