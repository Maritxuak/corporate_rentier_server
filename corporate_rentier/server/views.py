from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from rest_framework import status



class DignitiesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dignities.objects.filter(is_active=True)
    serializer_class = DignitiesSerializer


class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class DcsCatServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DcsCatServices.objects.filter(is_active=True)
    serializer_class = DcsCatServicesSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Projects.objects.filter(is_active=True)
    serializer_class = ProjectsSerializer

    @action(methods=['get'], detail=True)
    def similar(self, request, pk=None):
        try:
            project = Projects.objects.get(pk=pk)
            category_services_id = project.category_services.id
            similar_projects = Projects.objects.filter(category_services=category_services_id)
            serializer = ProjectsSerializer(similar_projects, many=True)
            return Response(serializer.data)
        except Projects.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class QuotesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer


class FeedBackCreateAPIView(generics.CreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer



class FeedBackListAPIView(generics.ListAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

