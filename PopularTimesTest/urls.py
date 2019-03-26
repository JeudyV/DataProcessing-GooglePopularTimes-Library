from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^map/',views.render_map),
    url(r'^place/',views.render_place),
    url(r'^getInfoURL/(?P<place_id>[\w{}.-]{1,40})',views.get_id),
]
