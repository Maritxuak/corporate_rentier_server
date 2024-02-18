from rest_framework import serializers
from .models import *


class DignitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dignities
        fields = ['id', 'name', 'dsc']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class DcsCatServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DcsCatServices
        fields = ['id', 'category', 'name', 'dsc']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'category_services', 'bw_preview_photo',
                  'c_preview_photo', 'title_photo', 'dsc_project', 'dsc_task',
                  'photo_task', 'dsc_realization', 'photo_realization', 'quotes']


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = '__all__'


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'



