from django.contrib import admin
from .models import *


admin.site.register(Filter)
admin.site.register(Status)
admin.site.register(PortfolioItem)
admin.site.register(PortfolioItemImage)
admin.site.register(Callback)