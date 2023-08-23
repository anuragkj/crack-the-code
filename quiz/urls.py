from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView
)
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('show-hint/<str:pk>/', views.showHint, name="show-hint"),
]