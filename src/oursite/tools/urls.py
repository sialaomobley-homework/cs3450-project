from django.urls import path
from . import views

app_name = 'tools'
urlpatterns = [
    path('', views.tools, name='tools'),
    path('<int:tool_id>/', views.tool_view, name='tool_view'),
]
