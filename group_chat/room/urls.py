from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.show_rooms, name='rooms'),
    path('<slug:slug>/', view=views.join_room, name='join_room')
]
