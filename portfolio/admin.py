from django.contrib import admin
from django.contrib import admin
from .models import Organization, Project, Skill, Honor, Course


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'start_date', 'end_date')
    list_filter = ('organization', 'start_date', 'end_date')
    search_fields = ('name', 'description', 'role')
    date_hierarchy = 'start_date'
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'role', 'organization', 'start_date', 'end_date', 'image', 'url', 'certificate')
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    list_filter = ('proficiency',)
    search_fields = ('name',)

@admin.register(Honor)
class HonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'organization')
    list_filter = ('date', 'organization')
    search_fields = ('name',)
    date_hierarchy = 'date'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'start_date', 'end_date')
    list_filter = ('institution', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'institution', 'start_date', 'end_date', 'certificate')
        }),
    )
