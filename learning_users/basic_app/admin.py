from django.contrib import admin
from basic_app.models import UserProfileInfo,Organization,Team,AgileTeam,Employee
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(AgileTeam)
admin.site.register(Employee)
#admin.site.register(User)
