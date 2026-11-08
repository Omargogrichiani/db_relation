from django.contrib import admin
from .models import Department, Student, StudentProfile, Course

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Course)