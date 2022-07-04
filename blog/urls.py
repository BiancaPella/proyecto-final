
from django.urls import path
from . import views
from .views import EditarPostView, PostsView, PostDetailView, PublicarView, EliminarPostView, ComentarView


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('posts', PostsView.as_view(), name="posts"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('publicar', PublicarView.as_view(), name='publicar'),
    path('post/editar/<int:pk>', EditarPostView.as_view(), name='editar'),
    path('post/eliminar/<int:pk>', EliminarPostView.as_view(), name='eliminar'),
    path('post/<int:pk>/comentar', ComentarView.as_view(), name='agregar_comentario'),
    path('resultado', views.resultado, name='resultado')
]
