from django.contrib import admin
from django.urls import path
from base.views import TaskList , TaskDetail, TaskCreate,TaskUpdate, TaskDelete, MyLoginView,Registerpage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register',Registerpage.as_view(), name = 'register' ),
    path('login', MyLoginView.as_view(), name = 'login' ),
    path('logout', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('', TaskList.as_view(), name = 'tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name = 'task' ),
    path('task-create', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name = 'task-update' ),
    path('task-delete/<int:pk>/',TaskDelete.as_view(), name = 'task-delete' ),
]
