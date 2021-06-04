from django.contrib import admin
from .models import Question,Choice,table,seller,verif,farmer,corporate,cart,feedback
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(table)
admin.site.register(seller)
admin.site.register(verif)
admin.site.register(farmer)
admin.site.register(corporate)
admin.site.register(cart)
admin.site.register(feedback)
# this is for registreing and editiable in admin page 127.0.0.1/.../admin/
