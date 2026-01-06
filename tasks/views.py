from django.shortcuts import render, redirect
from .models import Task 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import form 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasklist.html'
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form.TaskfilterForm(self.request.GET)
        return context
    def get_queryset(self):
        query_set = super().get_queryset()
        status = self.request.GET.get('status', '')
        priority = self.request.GET.get('priority', '')
        if status:
            query_set = query_set.filter(status = status)
        if priority:
            query_set = query_set.filter(priority = priority)
        
        return query_set


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'taskform.html'
    form_class = form.TaskForm
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class EditMode(UpdateView):
    model = Task
    form_class = form.TaskForm
    template_name = 'Edit.html'
    success_url = reverse_lazy('task-list')

class DeleteMode(DeleteView):
    model = Task
    template_name = 'Delete.html'
    success_url = reverse_lazy('task-list')

class Logoutuser(LogoutView):
    next_page = 'task-list'

class Loginuser(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class Registeruser(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy('task-list'))
    
