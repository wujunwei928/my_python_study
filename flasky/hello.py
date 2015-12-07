
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

# index page
@app.route('/')
def index():
    # if user login, redirect to /crontab/list, else redirect to /user/login
    # return '<h1>Hello World!</h1>'
    return render_template('index.html')

user register
@app.route('/user/register')
def user_register():
    # return '<h1>user register!</h1>'
    return render_template('user_register.html')

# user login
@app.route('/user/login')
def user_login():
    # return '<h1>user login!</h1>'
    return render_template('user_login.html')

# crontab list
@app.route('/crontab/list')
def crontab_add():
    # return '<h1>crontab list!</h1>'
    return render_template('crontab_list.html')

# add crontab
@app.route('/crontab/add')
def crontab_add():
    # return '<h1>crontab add!</h1>'
    return render_template('crontab_add.html')

# update crontab
@app.route('/crontab/update/<crontab_id>')
def crontab_update(crontab_id):
    # return '<h1>Hello, %s!</h1>' % crontab_id
    return render_template('crontab_update.html')

# 404 page
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# 500 page
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
