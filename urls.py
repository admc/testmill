#   Copyright 2009, Adam Christian (adam@adamchristian.com) and Slide, Inc.
#	
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#	
#           http://www.apache.org/licenses/LICENSE-2.0
#	
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^testMill/', include('testMill.foo.urls')),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    #projects
    (r'^projects/', include('projects.urls')),
    
    #accounts
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    (r'^accounts/logout/$', 'testMill.accounts.views.logout_view'),
        
    #static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static', 'show_indexes': True}),
    
    #default
    (r'^$','testMill.projects.views.index'),
)
