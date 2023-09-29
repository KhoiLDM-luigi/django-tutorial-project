from . import views
from django.urls import path

urlpatterns = [
    path('questions/', views.QuestionsView.as_view()),
    path('questions/<int:id>/', views.QuestionsView.as_view()),
    path('answers/', views.AnswerView.as_view()),
    path('answers/<int:id>/', views.AnswerView.as_view()),
]
