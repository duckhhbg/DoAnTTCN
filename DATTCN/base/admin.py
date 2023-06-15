from django.contrib import admin
from .models import Quanhuyen,Xaphuong,Duan,Duongpho

# Register your models here.

admin.site.register(Quanhuyen)
admin.site.register(Xaphuong)
admin.site.register(Duongpho)
admin.site.register(Duan)