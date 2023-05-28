from django.contrib import admin

from ArtyProd.models import Client

from .views import *

admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
admin.site.register(Client)
admin.site.register(Team)

