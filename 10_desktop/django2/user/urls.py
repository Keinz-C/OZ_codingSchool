from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
]