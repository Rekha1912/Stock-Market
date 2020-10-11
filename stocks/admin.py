from django.contrib import admin
from .models import Userstock , Cash, StockQuantity

admin.site.register(Userstock)
admin.site.register(Cash)
admin.site.register(StockQuantity)