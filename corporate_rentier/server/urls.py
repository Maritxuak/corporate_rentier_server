from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'dignities', DignitiesViewSet)
router.register(r'services', ServicesViewSet)
router.register(r'dcsCatServices', DcsCatServicesViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'quotes', QuotesViewSet)

urlpatterns = [
    path('read/', include(router.urls)),
    path('create/FeedBack', FeedBackCreateAPIView.as_view()),
    path('read/FeedBack', FeedBackListAPIView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)