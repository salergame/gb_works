from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        number = int(request.form['number'])
        square = number ** 2
        return redirect(url_for('show_result', number=number, square=square))

@app.route('/show_result/<int:number>/<int:square>')
def show_result(number, square):
    return render_template('result.html', number=number, square=square)

if __name__ == '__main__':
    app.run(debug=True)
