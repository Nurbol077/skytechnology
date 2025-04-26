from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PlaceViewSet, TimeSlotViewSet, BookingListCreateView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'timeslots', TimeSlotViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('booking/', BookingListCreateView.as_view(), name='booking')
]
