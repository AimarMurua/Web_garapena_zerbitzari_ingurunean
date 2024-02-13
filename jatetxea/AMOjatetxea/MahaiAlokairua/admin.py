from django.contrib import admin
from .models import Mahaia
from .models import Bezeroa
from .models import Alokairua

# Register your models here.

admin.site.register(Mahaia)
admin.site.register(Bezeroa)
admin.site.register(Alokairua)