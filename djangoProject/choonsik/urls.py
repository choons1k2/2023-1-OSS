from django.urls import path
from . import views

app_name = 'choonsik'

urlpatterns = [
    path('', views.home, name='home'),
    path('free_board/', views.free_board, name='free_board'),
    path('free_board/new_post/', views.new_post, name='new_post'),
]
