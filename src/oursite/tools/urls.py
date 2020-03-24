from django.urls import path
from . import views

app_name = 'tools'
urlpatterns = [
    path('', views.tools, name='tools'),
    path('<int:tool_id>/', views.tool_view, name='tool_view'),
    path('blog', views.BlogView.as_view(), name = 'blog'),
    path('blog/<int:pk>/', views.EntryView.as_view(), name = 'entry'), 
]
