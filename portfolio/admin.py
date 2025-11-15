from django.contrib import admin

from .models import Project, Skill, Experience, BlogPost, ContactMessage

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created')
    search_fields = ('title', 'short_description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'published')

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at', 'read')
    list_filter = ('read', 'sent_at')
