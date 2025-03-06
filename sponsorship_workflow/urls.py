from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sponsors', views.sponsors),
    path('<int:id>/', views.details, name='details'),
    path('create', views.create_sponsor, name='create_sponsor'),
    path('add', views.add_sponsor, name='add_sponsor')
]
