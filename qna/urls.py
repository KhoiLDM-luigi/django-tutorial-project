from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.QuestionView.as_view(), name='question'),
    path("", views.QnAView.as_view(), name='index')
]
