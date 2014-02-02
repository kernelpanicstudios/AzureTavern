from django.conf.urls import patterns, include, url
from .views import (HomeView, LoginView, LogoutView, RegisterView,
    RegistrationCompleteView)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),

    # Registration/login
    url(r'^account/login$', LoginView.as_view(), name='login'),
    url(r'^account/logout$', LogoutView.as_view(), name='logout'),
    url(r'^account/register$', RegisterView.as_view(), name='register'),
    url(r'^account/created$',
        RegistrationCompleteView.as_view(),
        name='registration_complete'
    )

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
