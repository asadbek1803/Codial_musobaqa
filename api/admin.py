from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import TestModel, Sohalar

# Register your models here.
@admin.register(TestModel)
class TestModelAdmin(ModelAdmin):
    list_display = ('id', 'test_name', 'test', 'correct_answer', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    list_editable = ('correct_answer',)
    list_display_links = ('id', 'test_name',)
    search_fields = ('test_name', 'test')


@admin.register(Sohalar)
class SohalarAdmin(ModelAdmin):
    list_display = ('id', 'name', )
    list_filter = ('id', )

    list_display_links = ('id', 'name')
    search_fields = ('name', )
