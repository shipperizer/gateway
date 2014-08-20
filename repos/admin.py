from django.contrib import admin
from repos.models import Repo, File

class FileInline(admin.TabularInline):
	model = File
	extra = 2


class RepoAdmin(admin.ModelAdmin):
	fieldsets = [
		('General Info', {'fields':['name']}),
		#('General Info', {'fields':['id']}),
		]
	inlines = [FileInline]	
	list_display = ['name']
	list_filter = ['name']
	search_field = ['name']

admin.site.register(Repo,RepoAdmin)