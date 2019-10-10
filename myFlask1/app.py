"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

#初始化，赋予__name__决定flask程序的根目录
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

#路由和视图函数
@app.route('/')
def hello():
    #(DAY_1源代码）
    """Renders a sample page."""
    #return '<h1>"Hello World!"</h1>'
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)



#（未改的代码）
#if __name__ == '__main__':
#    import os
#    HOST = os.environ.get('SERVER_HOST', 'localhost')
#    try:
#        PORT = int(os.environ.get('SERVER_PORT', '5555'))
#    except ValueError:
#        PORT = 5555
#    app.run(HOST, PORT)


#启动服务器
if __name__ == '__main__' :
    app.run(debug=True)
