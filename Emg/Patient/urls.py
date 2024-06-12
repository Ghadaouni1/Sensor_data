from django.urls import path
from .views import PatientListCreateAPIView, PatientRetrieveUpdateAPIView

urlpatterns = [
    path('create/', PatientListCreateAPIView.as_view()),
    path('<str:full_name>/', PatientRetrieveUpdateAPIView.as_view(), name='patient-retrieve-update'),  # Handles GET, PUT, PATCH

]