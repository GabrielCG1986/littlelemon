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

class menuView(APIView):
    def get(self, request):
        queryset = Menu.objects.all()
        serialized_item = MenuSerializer(queryset, many=True)

        return Response(serialized_item.data, status=200)
    
    def post(self, request):
        serialized_item = MenuSerializer(data=request.data)

        if serialized_item.is_valid():
            serialized_item.save()

        return Response({'status': 'success', 'data': serialized_item.data})

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