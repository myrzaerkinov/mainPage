from django.contrib import admin
from . import models


admin.site.register(models.BusinessAccount)
admin.site.register(models.SalonReview)
admin.site.register(models.SalonService)
admin.site.register(models.Staff)
admin.site.register(models.StaffTimetable)
admin.site.register(models.StaffService)
admin.site.register(models.Interior)
admin.site.register(models.StaffWork)
admin.site.register(models.StaffReview)