from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.web_blog.urls')),
    path('register/', include('blog.users.urls'))
]
