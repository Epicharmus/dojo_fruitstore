from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    session['count'] = 0
    session['count'] += 1
    return session['count']


if __name__ == "__main__":
    app.run(debug=True)