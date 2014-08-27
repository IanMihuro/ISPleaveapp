#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.api import mail

import webapp2
import os
import logging
import csv

from google.appengine.api import rdbms
from google.appengine.ext import webapp
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google. appengine.ext import db
from google.appengine.api import mail
from google.appengine.ext.webapp import template

import jinja2
import re

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        url = users.create_login_url(self.request.uri)
        url_linktext = 'Login'


        if user:
        	url = users.create_logout_url(self.request.uri)
        	url_linktext = 'Logout'

        values = {
        	'url_linktext'	:	url_linktext,
        	'user' : user,
        	'url'	:	url
        	      }

        
        self.response.write(template.render('index.html', values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
