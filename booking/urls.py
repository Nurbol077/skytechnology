from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PlaceViewSet, TimeSlotViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'timeslots', TimeSlotViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
