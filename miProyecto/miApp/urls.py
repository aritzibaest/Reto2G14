from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('departamento/<int:departamento_id>',views.departamento, name='detail'),
    path('empleado/<int:empleado_id>', views.empleado, name='detail')
]
