from flask import Flask,session,g,render_template
from jinja2 import Undefined

class NullUndefined(Undefined):
    def __str__(self):
        return '%s doesnt exist so we give you this'%self._undefined_name
    def __int__(self):
        return (9999999)
    def __float__(self):
        return 999999.0
    __iter__ = Undefined._fail_with_undefined_error


class NullFlask(Flask):
    # 给模板添加一个错误处理类，当没有找到参数就调用这个？
    jinja_options = dict(
        autoescape=True,
        extensions=['jinja2.ext.autoescape', 'jinja2.ext.with_'],
        undefined=NullUndefined
    )

app = NullFlask(__name__)
# 给模板增加int和float方法
app.jinja_env.globals.update(int=int, float=float)
app.secret_key = b'key'

@app.route('/<param>/')
def home(param):
    g.param = param
    session['dada'] = param
    return render_template('index.html', param=param)

def get_it():
    g.param = '000000'

@app.route('/a/')
def sec():
    name = session['dada']
    get_it()
    return render_template('name.html', )



if __name__ == '__main__':
    app.run(debug=True)