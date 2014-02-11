from django.contrib import admin
from formobile.models import Site, Entry
# Register your models here.

class EntryInline(admin.StackedInline):
	"""Arrange Entry in StackedInline mode."""
	model = Entry
	extra = 0

class EntryAdmin(admin.ModelAdmin):
	"""AdminSite for Entries"""
	fields = ['title', 'author', 'published', 'summary', 'link', 'content_value', 'site']

class SiteAdmin(admin.ModelAdmin):
	"""AdminSite for Sites"""
	fields = ['name', 'url', 'updated_ts']
	inlines = [EntryInline]

admin.site.register(Site, SiteAdmin)
admin.site.register(Entry, EntryAdmin)
