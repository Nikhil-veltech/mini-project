from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import urllib.parse

app = Flask(__name__)

password = urllib.parse.quote_plus("Vtu@26790")
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{password}@localhost/todo_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# MODEL
class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    beginning_date = db.Column(db.Date, nullable=False)
    deadline = db.Column(db.Date, nullable=False)
    completed = db.Column(db.Boolean, default=False)

# CREATE TABLE
with app.app_context():
    db.create_all()

# HOME
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# ADD TASK
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task']
    amount = float(request.form['amount'])
    beginning_date = request.form['beginning_date']
    deadline = request.form['deadline']

    beginning_date = datetime.strptime(beginning_date, '%Y-%m-%d').date()
    deadline = datetime.strptime(deadline, '%Y-%m-%d').date()

    new_task = Task(
        task=task_name,
        amount=amount,
        beginning_date=beginning_date,
        deadline=deadline
    )

    db.session.add(new_task)
    db.session.commit()

    return redirect('/')

# COMPLETE TASK
@app.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get(id)
    task.completed = True
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)