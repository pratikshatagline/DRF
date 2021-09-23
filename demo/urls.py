from django.urls import path
from . import views
from .views import RegisterView, LoginAPIView, RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView

urlpatterns = [
    path('', views.apiOverView, name="apiOverView"),
    path('task-list/', views.taskList, name="taskList"),
    path('task-detail/<str:pk>/', views.taskDetail, name="taskDetail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="taskUpdate"),
    path('task-create/', views.taskCreate, name="taskCreate"),
    path('task-delete/<str:pk>/', views.taskDelete, name="taskDelete"),
    path('tasklist/', views.tasklist.as_view(), name="taskList"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]