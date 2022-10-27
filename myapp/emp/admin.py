from django.contrib import admin
from .models import Emp,Testimonial

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','phone')


admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)
# Register your models here.
