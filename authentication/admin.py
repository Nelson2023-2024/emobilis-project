from django.contrib import admin
from authentication.models import User,Category,Contact
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Contact)