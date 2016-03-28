from django.contrib import admin

# Register your models here.
from subject.models import Subject,  Page


class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Page)
