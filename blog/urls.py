"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# 'include' allows us to include extra url files

from django.conf.urls import url, include
from django.contrib import admin


# 'RedirectView' allows us to redirect to a view

from django.views.generic import RedirectView

# Import serve

from django.views.static import serve

# Import MEDIA_ROOT - this is how we're going to serve out our media URL

from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # This is our root directory - so if someone wants to go to our root
    # directory, we want to redirect them to Posts. This means that when you
    # click on the link in the terminal window, it will append '/posts' to the
    # url - e.g.: 
    # https://fe73773e0b8047949f0bc75559273b50.vfs.cloud9.us-east-1.amazonaws.com/posts/
    
    url(r'^$', RedirectView.as_view(url='posts/')),
    
    # If a user goes to the posts url, we want to be passed using the urls in
    # the posts/urls.py file
    
    url(r'posts/', include('posts.urls')),
    
    # Media - we indicate the start of the line with '^', and we can point 
    # towards a path to a particlar file, and we're going to use the 'serve'
    # library, and we serve up document root that we imported from settings.py
    # above
    
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]


