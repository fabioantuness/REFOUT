
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('notifications', views.notifications, name='notifications'),
    path('profile', views.profile, name='profile'),
    path('post', views.post, name='post'),
]