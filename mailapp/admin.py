from django.contrib import admin
from .models import Mailbox, Template, Email
# Register your models here.

admin.site.register(Mailbox)
admin.site.register(Template)
admin.site.register(Email)
