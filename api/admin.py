from django.contrib import admin

from .models import team, match

# Register your models here.
class teamAdmin(admin.ModelAdmin):
    list_display = ('teamName', 'teamNumber', 'avgScore')


admin.site.register(team, teamAdmin)
admin.site.register(match)
