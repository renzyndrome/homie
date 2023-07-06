from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('myadmin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Homie Admin"
admin.site.site_header = "Homie Admin Portal"
admin.site.site_header = "Welcome to Homie"