from django.contrib import admin
from .models import user, phone_brand, phone_modell, phone_feature, phone_feature_v, tab_brand, tab_modell, tab_feature, \
    tab_feature_v, watch_brand, watch_modell, watch_feature, watch_feature_v

# Register your models here.
admin.site.register(user)
admin.site.register(phone_brand)
admin.site.register(phone_modell)
admin.site.register(phone_feature)
admin.site.register(phone_feature_v)
admin.site.register(tab_brand)
admin.site.register(tab_modell)
admin.site.register(tab_feature)
admin.site.register(tab_feature_v)
admin.site.register(watch_brand)
admin.site.register(watch_modell)
admin.site.register(watch_feature)
admin.site.register(watch_feature_v)


