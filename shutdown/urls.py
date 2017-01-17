from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_controls, name='show_controls'),
    url(r'^suspend/', views.suspend, name='suspend'),
]
