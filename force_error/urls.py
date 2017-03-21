from django.conf.urls import url

from . import views

app_name = 'force_error'
urlpatterns = [
    url(r'^error/$', views.force_error_view, name='error'),
    url(r'^permission_denied/$', views.force_permission_denied_view,
        name='permission_denied'),
]
