from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.ProductImg)
admin.site.register(models.ProductVideo)
admin.site.register(models.Review)
admin.site.register(models.Cart)
admin.site.register(models.CartProduct)