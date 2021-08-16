from django.urls import path
from .views import people

urlpatterns = [
    path('people/', people),
    path('people/<int:num>', people),
]
