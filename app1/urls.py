from django.urls import path
from . import views

urlpatterns = [
    path('first',views.index,name='index'),
    path('resume',views.resume,name='resume'),
    path('table',views.book,name='book'),
]
