from django.contrib import admin
# from firstapp.views import complaint, contact
from firstapp.models import Complaint, Signup
from .models import Accounts
# Register your models here.

admin.site.register(Complaint)
admin.site.register(Signup)
admin.site.register(Accounts)