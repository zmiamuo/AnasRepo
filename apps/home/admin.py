

from django.contrib import admin
from .models import website
from .models import DurationUsage
from .models import Availaible_ip
from .models import logs_generated

from .models import logs_json

class Adminwebsite(admin.ModelAdmin):
    model = website
    list_display = ('id','author', 'website_url', 'website_blocked')


admin.site.register(website, Adminwebsite)

class AdminDurationUsage(admin.ModelAdmin):
    model = DurationUsage
    list_display = ('id','author', 'duration', 'usage','ip_address')

admin.site.register(DurationUsage,AdminDurationUsage)

class AdminAvailable_ip(admin.ModelAdmin):
    model = Availaible_ip
    list_display = ('id','Availaible_ip')
admin.site.register(Availaible_ip,AdminAvailable_ip)


class Adminlogs_generated(admin.ModelAdmin):
    model = logs_generated
    list_display = ('id','date','ip_address_src','ip_address_dst','action')
admin.site.register(logs_generated,Adminlogs_generated)


class Adminlogs_json(admin.ModelAdmin):
    model = logs_json
    list_display = ('id','author',"lenght", "Layer_ETH", "Layer_IP", "Layer_UDP","Layer_ARP","Layer_TCP","Layer_TLS","Layer_DNS")
admin.site.register(logs_json,Adminlogs_json)


