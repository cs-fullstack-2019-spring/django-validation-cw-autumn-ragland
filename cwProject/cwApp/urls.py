from django.urls import path
from . import views

urlpatterns = [
    # on load path
    path('', views.index, name='index'),
    # second path
    path('submit', views.submission, name='submit')
]
