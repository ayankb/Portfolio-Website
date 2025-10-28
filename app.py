from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'bd83y7dhbh81w21q'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
