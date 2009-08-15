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

from django.db import models
from django.contrib import admin

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


# Create your models here.
class Server(models.Model):
    SERVER_CHOICES = (
        ('TRAC','TRAC'),
        ('HUDSON','HUDSON'),
        ('SOURCE','SOURCE'),
        ('COUCHDB','COUCHDB'),
    )
    name = models.CharField(max_length=30, choices=SERVER_CHOICES)
    path = models.CharField(max_length=255)

class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'path')


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Server, ServerAdmin)