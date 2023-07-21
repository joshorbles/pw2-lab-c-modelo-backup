from django.urls import path
from tutorial.quickstart import views  # No necesitas importar 'views' dos veces

urlpatterns = [
    path('grupos/', views.GroupListView, name='mostrar_grupos'),
    path('grupos/<uuid:group_id>/alumnos/', views.StudentInGroupListView, name='alumnos_inscritos')