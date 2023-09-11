from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Player


class PlayerListView(LoginRequiredMixin, ListView):
    model = Player
    template_name = 'player/list.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.filter(user=self.request.user)
    
class PlayerCreateView(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'institute_id', 'contact']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)