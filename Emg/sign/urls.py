from django.urls import path
from django.urls import path, include

urlpatterns = [
    # other urlpatterns specific to the 'sign' app
    path('auth/', include('djoser.urls')),  # Djoser's authentication endpoints
    path('auth/', include('djoser.urls.jwt')),  # JWT authentication endpoints
]
