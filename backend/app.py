from flask import Flask, request, jsonify, g
import sqlite3
from datetime import datetime

DB_PATH = 'procurement.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        requester TEXT,
        department TEXT,
        item_name TEXT,
        quantity INTEGER,
        justification TEXT,
        status TEXT,
        created_at TEXT
    )
    ''')
    db.commit()

@app.route('/api/requests', methods=['GET'])
def list_requests():
    db = get_db()
    cursor = db.execute('SELECT * FROM requests ORDER BY created_at DESC')
    rows = cursor.fetchall()
    return jsonify([dict(r) for r in rows])

@app.route('/api/requests', methods=['POST'])
def create_request():
    data = request.json or {}
    required = ['requester','department','item_name','quantity','justification']
    if not all(k in data for k in required):
        return jsonify({'error':'missing fields'}), 400
    db = get_db()
    now = datetime.utcnow().isoformat()
    cursor = db.execute(
        'INSERT INTO requests (requester,department,item_name,quantity,justification,status,created_at) VALUES (?,?,?,?,?,?,?)',
        (data['requester'],data['department'],data['item_name'],int(data['quantity']),data['justification'],'PENDING',now)
    )
    db.commit()
    rid = cursor.lastrowid
    cursor = db.execute('SELECT * FROM requests WHERE id=?',(rid,))
    row = cursor.fetchone()
    return jsonify(dict(row)),201

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(host='0.0.0.0',port=5000,debug=True)