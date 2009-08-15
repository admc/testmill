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
urlpatterns = patterns('testMill.projects.views',
    (r'^doc/(?P<id>\w+)/','detail'),
    (r'^new','new'),
    (r'^view','view'),
    (r'^feed','feed'),
    (r'^url','url'),
    (r'^list','list'),
    (r'^get_cases','get_cases'),
    (r'^save_cases','save_cases'),
    (r'^delete_case','delete_case'),
    (r'^tree','tree'),
    (r'^get_file_source', 'get_file_source'),
    (r'^$','index'),
)