"""
small flaks app implements some features such as
session, cookie, g
"""
import sqlite3
import os
from json import dumps, loads
from flask import (Flask, request, session, g,
    render_template, redirect)
from werkzeug.contrib.sessions import SessionStore, Session
from werkzeug.contrib.securecookie import SecureCookie


create_database = """
    create table session (
    id integer primary key autoincrement,
    session_id text not null,
    'session_content' text not null
    );
    """

class SqliteSessionStore(SessionStore):
    # 自定义sqlite数据库实现的session存储
    # 继承自sessionseotr，实现save、delete、get方法

    def __init__(self, session_class=None):
        if session_class is None:
            session_class = Session
        SessionStore.__init__(self, session_class)
        self.session_class = session_class

    def save(self, session):
        # 这个方法通常在构造完response后调用，所以直接调用
        # 系统的db或者g，是没有问题得
        db = connect_db()
        SQL = """INSERT INTO session
                    (session_id, session_content)
                VALUES 
                    (?, ?)
                """
        db.execute(SQL, (session.sid, dumps(dict(session))))
        db.commit()


    def delete(self, session):
        db = connect_db()
        SQL = """
                DELETE FROM session;
                WHERE session_id = ?
            """
        db.execute(SQL, (session.sid))
        db.commit()

    def get(self, sid):
        # 而这个方法，有时候在构造请求环境的时候就调用，此时还没有g对象
        # 所以需要单独构造数据库连接。
        if not self.is_valid_key(sid):
            return self.new()
        DATABASE_PATH = os.path.join(app.root_path, 'session.sqlite')
        db = sqlite3.connect(DATABASE_PATH)
        SQL = """
                SELECT * FROM session WHERE session_id = ?
            """
        session_data = db.execute(SQL, (sid,))
        session_data = session_data.fetchone()[2]
        db.close()
        if session_data is not None:
            session_data = loads(session_data)
        else:
            session_data = {}
        return self.session_class(session_data, sid)



# 实现自己的session实现，利用sqlite
class SqliteSessionFlask(Flask):
    # 原理是：将session内存储在数据库上，有一个专门的标识，比如ID的SHA值
    # 然后将SHA值以COOKIE形式存储在客户端
    # w问题是，如何将ID的SHA值以securecookie的形式存储？
    # 系统原本的session是如何实现的？
    # 原系统里，将cookie里存储为session名字的session内容，传入SecureCookie，
    # 再额外给定一个secret_key，然后再将这个SecureCookie对象序列化，默认使用
    # pickle序列化，并用SHA1计算校验值
    # open_session是获取一个SecureCOOkie对象，而save_session，则如果SecureCookue
    # 对象的modified为TRUE，则调用save_cookie方法，词方法再次调用response对象的
    # set_cookie方法，以实现保存

    def __init__(self, package_name):
        Flask.__init__(self, package_name)
        self.session_store = SqliteSessionStore()

    def open_session(self, request):
        # 这里的逻辑是，在构建请求环境的时候，用secure_cookie.load_cookie从
        # 请求中加载session内容，从中读取出sid值，再根据sid从数据库中读取session
        # 真正的内容，并用这些内容构建一个真正的，在视图函数中使用的session对象
        # 这个函数的返回值会成为_request_ctx_stack的栈顶的session对象
        key = self.secret_key
        if key is not None:
            secure_cookie = SecureCookie.load_cookie(request, self.session_cookie_name,
                                            secret_key=self.secret_key)
            sid = secure_cookie.get('sid')
            if sid is not None:
                request_session = self.session_store.get(sid)
            else:
                request_session = self.session_store.new()
            return request_session

    def save_session(self, session, response):
        # 这个函数将在构造好了response后调用，此函数逻辑是如何session有内容，就将其
        # 保存在数据库，然后构建一个新的Securecookie，在传入sid的值，然后保存在response
        # 中
        if session is not None:
            if session.should_save:
                self.session_store.save(session)

            secure_cookie = SecureCookie({}, secret_key=self.secret_key)
            secure_cookie['sid'] = session.sid
            # 这里必须要有一次额外的赋值，否则secure_cookie的should_save为False
            secure_cookie.save_cookie(response, self.session_cookie_name)


app = SqliteSessionFlask(__name__)
app.secret_key = b'tss'

def connect_db():
    DATABASE_PATH = os.path.join(app.root_path, 'session.sqlite')
    if not hasattr(g, 'db'):
        rv = sqlite3.connect(DATABASE_PATH)
        rv.row_factory = sqlite3.Row
        g.db = rv
        return rv
    return g.db

@app.before_request
def get_db():
    connect_db()

@app.after_request
def close_db(response):
    if hasattr(g, 'db'):
        g.db.close()
    return response

def init_db():
    DATABASE_PATH = os.path.join(app.root_path, 'session.sqlite')

    db = sqlite3.connect(DATABASE_PATH)
    db.cursor().executescript(create_database)
    db.commit()
    db.close()
    print ('create the db !')

@app.route('/<int:param>/')
def home(param):
    html = render_template('index.html', param=param)
    resp = app.make_response(html)
    session['param'] = param
    resp.set_cookie('TEST', 'VALUE')
    return resp

@app.route('/ts/')
def test():
    # param = g.param
    param = session.get('param')
    print ('PARAM IS ',param)
    def func(num):
        return int(num) + 10
    return render_template('name.html', name=param, func=func)

if __name__ == '__main__':
    #init_db()
    app.run(debug=True)

def test_func(x):
    return 'yes we get ',x

