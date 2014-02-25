from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from .views import (HomeView, LogoutView, RegisterView,
    RegistrationCompleteView)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),

    # RPTavern URLs (the main application)
    url(r'^rp/', include('rptavern.urls')),

    # Registration/login
    url(r'^account/login$', login,
        {'template_name': 'accounts/login.html'},
        name='login',
    ),
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
