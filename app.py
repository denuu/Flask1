from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # return do_the_login()
        return 'login'
    else:
        # return show_the_login_form()
        return 'not log in'

@app.route('/user/<username>')
def profile(username):
    # show relavant user profile
    return '{}\'s profile'.format(username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show post with given int ID
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath

# converter types: string (default), int, float, path, uuid

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

# url_for('static', filename='style.css')