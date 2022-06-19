from django.urls import path, include
from .views import *

urlpatterns = [
    path("test/", plot_graph, name="home"),
    path('', main, name="main")
]
