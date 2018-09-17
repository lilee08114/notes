from werkzeug import import_string, cached_property

path = 'pss.SqliteSessionStore'

class FakeFunc:
	def __init__(self, path):
		self.__module__, self.__name__ = path.rsplit('.', 1)
		self.path = path

	@cached_property
	def view(self):
		return import_string(self.path)

	def __call__(self, *args, **kwargs):
		return self.view(*args, **kwargs)

a = FakeFunc('pss.test_func')
print (a.__name__)
print (a)