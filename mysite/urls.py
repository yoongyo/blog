from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.main, name="main"),
    re_path(r'^blog/', include(('blog.urls', 'blog'), namespace='blog'))
]
