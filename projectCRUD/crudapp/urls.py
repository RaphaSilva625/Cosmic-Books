from django.urls import path, include
from . import views, admin

app_name='crudapp'

urlpatterns = [
    path('index', views.index, name='index'),
    path('create_template', views.create_template, name='create_template'), #Será o nosso formulário
    path('create', views.create, name='create'),
    path('update_template/<int:livro_id>', views.update_template, name="update_template"),
    path('update', views.update, name="update"),
    path('delete/<int:livro_id>', views.delete, name="delete"),
    path('home', views.home, name="home"),
    path('contato', views.contato, name='contato'),
    path('estoque', views.estoque, name="estoque"),
    path('equipe', views.equipe, name="equipe")
]