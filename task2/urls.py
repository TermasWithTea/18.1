from django.urls import path
from .views import func, Class

urlpatterns = [
    path('function/', func, name='function_view'),
    path('class/', Class.as_view(), name='class_view'),
]