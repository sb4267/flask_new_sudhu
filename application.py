from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return render_template('hello.html')

@app.route('/myapp', methods=['POST', 'GET'])
def second_page():
    if request.method == 'POST':
        return render_template('result.html', result=request.form['uname'])
    return render_template('result.html', error="error")

if __name__ == '__main__':
    app.run(debug=False)
