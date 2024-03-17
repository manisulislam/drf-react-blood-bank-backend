
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/',include('accounts.urls')),
    path('api/v1/',include('contact.urls')),
    path('api/v1/',include('blood_app.urls')),
    path('api/v1/',include('blog.urls'))
]
