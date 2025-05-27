from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, BatchEventCreateView, EventViewSet, ShareEventView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('events/batch/', BatchEventCreateView.as_view(), name='event-batch-create'),
    path('events/<int:id>/share/', ShareEventView.as_view(), name='share-event'),

    # ✅ Include router URLs inside the list
    path('', include(router.urls)),
]
