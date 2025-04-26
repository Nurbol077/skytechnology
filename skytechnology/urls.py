from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Booking API",
        default_version='v1',
        description="API для бронирования мест",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@booking.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,  # Разрешаем публичный доступ
    permission_classes=[permissions.AllowAny],  # Убираем ограничения на доступ
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls')),
    path('swagger/', schema_view.as_view()),  # Swagger-документация
]
