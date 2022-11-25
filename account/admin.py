from django.contrib import admin
from account.models import User, Role, UserProfile
from django.contrib.auth.models import Group

admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserProfile)
admin.site.unregister(Group)

