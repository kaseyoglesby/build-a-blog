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
import webapp2, os, jinja2, cgi

template_directory = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory))

# Used Handler class from https://classroom.udacity.com/courses/cs253/lessons/676928821/concepts/6865988250923#
# Hander class defines template rendering in order to make it easier within other Handlers/Methods
# Instructor granted permission to use freely

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class EntryPoint(Handler):
	def get(self):
		self.render("front.html")


class MainHandler(Handler):
    def get(self):
    	self.render("base.html")

app = webapp2.WSGIApplication([
    ('/blog', MainHandler),
    ('/', EntryPoint)
], debug=True)
