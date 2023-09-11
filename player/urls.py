from django.urls import path
from .views import (
    PlayerListView,
    PlayerCreateView
)

urlpatterns = [
    path('', PlayerListView.as_view(), name='player-list'),
    path('new/', PlayerCreateView.as_view(), name='player-create')
]