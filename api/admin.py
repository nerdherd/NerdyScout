from django.contrib import admin

from .models import team, match

# Register your models here.
class teamAdmin(admin.ModelAdmin):
    list_display = ('teamName', 'teamNumber', 'avgScore')

class matchAdmin(admin.ModelAdmin):
    list_display = ('matchNumber', 'team', 'alliance', 'score')

admin.site.register(team, teamAdmin)
admin.site.register(match, matchAdmin)
