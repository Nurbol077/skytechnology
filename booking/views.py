from rest_framework import viewsets, filters
from .models import Category, Place, TimeSlot, Booking
from .serializers import CategorySerializer, PlaceSerializer, TimeSlotSerializer, BookingSerializer
from rest_framework import serializers


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


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Убедитесь, что добавлен queryset
    serializer_class = BookingSerializer
