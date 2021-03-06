from django.contrib import admin
from models import Node, Route, Time

# class TimeInline(admin.TabularInline):
#     model = Time

class NodesAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

class RoutesAdmin(admin.ModelAdmin):
    list_display = ('start', 'destination')
    # inlines = [TimeInline]

admin.site.register(Node, NodesAdmin)
admin.site.register(Route, RoutesAdmin)
admin.site.site_header = 'Shuttle Management System'
