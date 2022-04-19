from flask import Flask, request, render_template, redirect


app = Flask(__name__)


@app.route('/')
def log_in():
    return render_template('login.html')


@app.route('/sign_up')
def reg_page():
    return render_template('sign_up.html')


if __name__ == '__main__':
    app.run()
