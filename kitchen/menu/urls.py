from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name="index"),
    path('user_feedback', views.user_feedback, name="user_feedback"),
]

urlpatterns += staticfiles_urlpatterns()