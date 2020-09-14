
from django.contrib import admin
from django.urls import re_path

from core.views import index


urlpatterns = [
    re_path("^admin/?", admin.site.urls),
    re_path("^/?$", index),
]
