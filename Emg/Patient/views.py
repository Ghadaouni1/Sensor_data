from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated access

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PatientListSerializer
        return PatientSerializer
    
class PatientRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny] 

    def get_object(self):
        full_name = self.kwargs.get('full_name')
        return generics.get_object_or_404(Patient, full_name=full_name)