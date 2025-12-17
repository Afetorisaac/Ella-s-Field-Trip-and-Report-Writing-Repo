from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
DB = os.path.join(os.path.dirname(__file__), 'ella.db')

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS requests
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, department TEXT, requester TEXT, status TEXT, created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, role TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS actions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, request_id INTEGER, action TEXT, actor TEXT, ts TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT id, title, department, requester, status, created_at FROM requests ORDER BY id DESC')
    requests_list = c.fetchall()
    c.execute('SELECT id, name, role FROM users')
    users = c.fetchall()
    conn.close()
    return render_template('admin.html', requests=requests_list, users=users)

@app.route('/create_request', methods=['POST'])
def create_request():
    title = request.form.get('title')
    department = request.form.get('department')
    requester_ = request.form.get('requester')
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('INSERT INTO requests (title, department, requester, status, created_at) VALUES (?, ?, ?, ?, ?)',
              (title, department, requester_, 'Pending', datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

@app.route('/register_user', methods=['POST'])
def register_user():
    name = request.form.get('name')
    role = request.form.get('role')
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('INSERT INTO users (name, role) VALUES (?, ?)', (name, role))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

@app.route('/simulate_send/<int:request_id>')
def simulate_send(request_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT title FROM requests WHERE id = ?', (request_id,))
    req = c.fetchone()
    request_title = req[0] if req else 'Unknown'
    c.execute('SELECT id, name, role FROM users')
    users = c.fetchall()
    conn.close()
    return render_template('simulate_send.html', request_id=request_id, request_title=request_title, users=users)

@app.route('/track/<int:request_id>/<int:user_id>')
def track(request_id, user_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT name FROM users WHERE id = ?', (user_id,))
    user = c.fetchone()
    actor_name = user[0] if user else 'Unknown'
    c.execute('INSERT INTO actions (request_id, action, actor, ts) VALUES (?, ?, ?, ?)',
              (request_id, 'Simulated action', actor_name, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
    return render_template('track.html', request_id=request_id)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
