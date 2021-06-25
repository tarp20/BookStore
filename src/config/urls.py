import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from store.views import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('auth/',auth),
    path('__debug__/', include(debug_toolbar.urls)),
]
