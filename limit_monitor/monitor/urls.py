from django.urls import path
from . import views

urlpatterns = [
    path('limit-list/', views.list_limits, name='list_limits'),
    path('create/', views.create_limit, name='create_limit'),
    path('update/<int:limit_id>/', views.update_limit, name='update_limit'),
    path('delete/<int:limit_id>/', views.delete_limit, name='delete_limit'),
]

