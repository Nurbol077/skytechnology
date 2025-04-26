from rest_framework import viewsets, filters
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions

from .models import Category, Place, TimeSlot, Booking
from .serializers import CategorySerializer, PlaceSerializer, TimeSlotSerializer, BookingSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['place__name', 'date']
    ordering_fields = ['date', 'start_time']

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.query_params.get('date')
        place_id = self.request.query_params.get('place_id')

        if date:
            queryset = queryset.filter(date=date)

        if place_id:
            queryset = queryset.filter(place_id=place_id)

        return queryset.filter(is_available=True)


class BookingListCreateView(ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
