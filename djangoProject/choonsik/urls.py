from django.urls import path

from . import views
from .views import CustomLoginView, CustomLogoutView, signup

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),

]

