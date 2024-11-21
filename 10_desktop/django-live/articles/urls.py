from django.urls import path
from . import views
urlpatterns = [
    # list - GET, 존재하는 article 보여주기
    path('', views.index, name='index'),
    # Create - POST, GET
    path('create/', views.create, name='create'),
    # Read - GET
    # path('<int:pk>/', views.detail, name='detail),
    # Update - POST, GET
    # path('<int:pk>/update/', views.update, name='update'),
    # Delete - POST, GET
    # path('<int:pk>/delete/', views.delete, name='delete'),
]