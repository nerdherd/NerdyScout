from django.contrib import admin

from .models import team, match

# Register your models here.
class teamAdmin(admin.ModelAdmin):
    list_display = ('teamNumber', 'avgScore')


admin.site.register(team, teamAdmin)
admin.site.register(match)
