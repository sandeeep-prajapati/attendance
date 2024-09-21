from django.contrib import admin
from import_export.admin import ExportMixin
from import_export import resources
from .models import Attendance, Hosteler

# Resource for exporting Attendance data
class AttendanceResource(resources.ModelResource):
    class Meta:
        model = Attendance
        fields = ('hosteler__name', 'hosteler__enrollment_number', 'date', 'is_present')
        export_order = ('hosteler__name', 'hosteler__enrollment_number', 'date', 'is_present')

# Resource for exporting Hosteler data
class HostelerResource(resources.ModelResource):
    class Meta:
        model = Hosteler
        fields = ('name', 'enrollment_number', 'room_number')
        export_order = ('name', 'enrollment_number', 'room_number')

# Customize the Admin Panel for Attendance
@admin.register(Attendance)
class AttendanceAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('hosteler', 'hosteler_enrollment_number', 'date', 'is_present')
    search_fields = ('hosteler__name', 'hosteler__enrollment_number')
    list_filter = ('date', 'is_present')
    resource_class = AttendanceResource
    date_hierarchy = 'date'
    list_per_page = 20
    ordering = ['-date']

    def hosteler_enrollment_number(self, obj):
        return obj.hosteler.enrollment_number
    hosteler_enrollment_number.short_description = 'Enrollment Number'

# Customize the Admin Panel for Hosteler
@admin.register(Hosteler)
class HostelerAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment_number', 'room_number')
    search_fields = ('name', 'enrollment_number')
    list_filter = ('room_number',)
    resource_class = HostelerResource
    list_per_page = 20

# Customize the Admin Panel for the Hostel
admin.site.site_header = "RK Boys Hostel Admin"
admin.site.site_title = "RK Boys Hostel Admin Portal"
admin.site.index_title = "Welcome to RK Boys Hostel Management"
