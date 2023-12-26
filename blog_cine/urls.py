from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.INICIO, name = 'INICIO' ),
    path('inicio/', views.INICIO, name = 'INICIO' ),
    path('contacto/', views.MOSTRARCONTACTO, name = 'CONTACTO' ),
    path('acercade/', views.MOSTRARACERCA, name = 'ACERCA'),
    path('agregar_post/', views.agregar_post, name='agregar_post'),
    
     #Urls de la aplicacion posts
    path('posts/', include('apps.posts.urls')),
    path('login/', LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout'),
    path('usuarios/', include('apps.usuarios.urls')),

] + static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
