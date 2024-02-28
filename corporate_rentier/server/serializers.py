from rest_framework import serializers
from .models import *


class DignitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dignities
        fields = ['id', 'name', 'category', 'dsc']


class DcsCatServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DcsCatServices
        fields = ['id', 'category', 'name', 'dsc']

class ServicesSerializer(serializers.ModelSerializer):
    included_in_the_service = DcsCatServicesSerializer(many=True, read_only=True)
    class Meta:
        model = Services
        fields = ['id', 'name', 'category', 'dsc', 'included_in_the_service']







class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    quotes = QuotesSerializer(many=True, read_only=True)
    class Meta:
        model = Projects
        fields = ['id', 'name', 'category_services', 'bw_preview_photo',
                  'c_preview_photo', 'title_photo', 'dsc_project', 'dsc_task',
                  'photo_task', 'dsc_realization', 'photo_realization', 'quotes']

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'



