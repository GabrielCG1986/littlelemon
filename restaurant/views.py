from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response 
from django.shortcuts import render
from rest_framework import generics
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer