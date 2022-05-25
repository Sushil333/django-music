from django.urls import path

from music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-favorite/', views.addToFevorite, name='add_to_favorite'),
    path('get-book/', views.getBook, name='get_book')
]