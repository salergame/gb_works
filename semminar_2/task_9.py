from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = redirect(url_for('welcome'))
        response.set_cookie('username', name)
        response.set_cookie('useremail', email)
        return response
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    response = redirect(url_for('index'))
    response.delete_cookie('username')
    response.delete_cookie('useremail')
    return response

if __name__ == '__main__':
    app.run(debug=True)
