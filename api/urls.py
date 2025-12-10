from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDeleteView.as_view(), name='task-detail'),
    path('auth/login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
