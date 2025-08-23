from django.contrib import admin
from .models import (
    PersonalInfo, Project, Skill, Education, 
    Certification, Testimonial, ContactMessage
)

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'location']
    search_fields = ['name', 'title', 'email']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']
    search_fields = ['name']
    list_editable = ['proficiency']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['institution', 'degree', 'field_of_study']
    list_editable = ['current']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date', 'expiry_date']
    list_filter = ['issue_date', 'expiry_date']
    search_fields = ['name', 'issuing_organization', 'credential_id']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'company', 'rating', 'featured', 'created_at']
    list_filter = ['rating', 'featured', 'created_at']
    search_fields = ['name', 'position', 'company', 'content']
    list_editable = ['rating', 'featured']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['read']
    readonly_fields = ['created_at']
    
    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    actions = ['mark_as_read'] 