import os
from werkzeug.wrappers import Response, Request	
from werkzeug.routing import Map, Rule
from jinja2 import Environment, FileSystemLoader

class App():	
	def __init__(self):
		# 绑定adaper、jinja+env
		self.url_map = Map([Rule('/', endpoint='vf_home'), 
			Rule('/<int:uid>/', endpoint='vf_user', methods=['POST'])])
		path = 'C:\\Users\\lilee\\Desktop\\fl\\templates'
		print ('path is ',path)
		self.jinja_env = Environment(loader=FileSystemLoader(path))

	def dispatch_request(self, request):
		# url路由到具体的视图函数，先绑定url_dapter到化境，然后匹配
		url_adapter = self.url_map.bind_to_environ(request.environ)
		v_func, args = url_adapter.match()
		print (v_func, args)
		resp = getattr(self, v_func)(request, **args)
		return resp

	def render_template(self, template_name, **context):
		template = self.jinja_env.get_template(template_name)
		return Response(template.render(**context, mimetype="text/html"))

	def vf_home(self, request, **args):
		if request.method == 'GET':
			return self.render_template('index.html', contents=request.headers)
		elif request.method == 'POST':
			return self.vf_user(request, **args)

	def vf_user(self, request, **args):
		if request.method == 'POST':
			uid = request.form.get('fname')
			return self.render_template('name.html', name=uid)

	def app(self, environ, start_response):
		request = Request(environ)
		response = self.dispatch_request(request)
		response.content_type = 'text/html; charset=utf-8'
		return response(environ, start_response)

	def __call__(self, environ, start_response):
		return self.app(environ, start_response)

def middle_ware(app):
	print ('we can do sth here')
	return app

def create_app():
	app = App()
	return middle_ware(app)

if __name__ == '__main__':
	app = create_app()
	from werkzeug.serving import run_simple
	run_simple('localhost', 5000, app, use_debugger=True)