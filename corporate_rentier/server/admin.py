from django.contrib import admin
from .models import *


class DcsCatServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['category', 'is_active']


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']


class DignitiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active']


class QuotesAdmin(admin.ModelAdmin):
    list_display = ['category', 'post', 'username']
    list_filter = ['category']


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_services']
    list_filter = ['category_services']


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['username', 'name_company', 'number_phone', 'category', 'data', 'is_processed']
    list_filter = ['category', 'data', 'is_processed', 'is_successfully']


admin.site.register(DcsCatServices, DcsCatServicesAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Dignities, DignitiesAdmin)
admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(FeedBack, FeedBackAdmin)


