from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# app.config['SQL_DATABASE_URI'] = "sqllite"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')


if __name__ == "__main__":
    app.run(debug=True)