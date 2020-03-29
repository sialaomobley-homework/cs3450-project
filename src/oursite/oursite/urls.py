"""oursite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from tools import views as tools_views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', tools_views.homepage, name='homepage'),
    path('toolview/', include('tools.urls')),
    path('tools', tools_views.tools, name = 'tools'),
    path('register/', user_views.register, name='register'),
    path('blog/', tools_views.BlogView.as_view(), name = 'blog'),
    path('blog/<int:pk>/', tools_views.EntryView.as_view(), name = 'entry'),
    path('blog/blogtest', tools_views.blogtest, name = 'blogtest'),
    path('contact/', tools_views.contact, name='contact'),
    path('about/', tools_views.about, name='about',)
        
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
