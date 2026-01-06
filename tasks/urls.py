from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name = 'task-list'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name = 'task-detail'),
    path('task/create/', views.TaskCreateView.as_view(), name = 'task-create'),
    path('taskmode/<int:pk>/', views.EditMode.as_view(), name = 'edit-task'),
    path('deletingtask/<int:pk>/', views.DeleteMode.as_view(), name = 'delete-task'),
    path('logout/', views.Logoutuser.as_view(), name = 'logout-user'),
    path('login/', views.Loginuser.as_view(), name = 'login-user'),
    path('register/', views.Registeruser.as_view(), name = 'register-user')
]