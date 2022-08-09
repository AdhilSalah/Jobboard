from django.contrib import admin

from mainuser.models import Education, Experience, NewUser, Userprofile

admin.site.register(NewUser)
admin.site.register(Userprofile)
admin.site.register(Education)
admin.site.register(Experience)
