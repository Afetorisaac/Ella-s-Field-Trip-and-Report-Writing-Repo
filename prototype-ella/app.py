"""
Ella's Procurement System Prototype
A minimal Flask demo for Korle-Bu Teaching Hospital procurement workflow
"""
from flask import Flask, request, jsonify, render_template_string, g
import sqlite3
from datetime import datetime
import os

# Database path
DB_PATH = 'ella.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# ============================================================================
# Database Helper Functions
# ============================================================================

def get_db():
    """Get database connection"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    """Close database connection at end of request"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """Initialize database with required tables"""
    db = get_db()
    cursor = db.cursor()
    
    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        full_name TEXT NOT NULL,
        role TEXT NOT NULL,
        department TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Create procurement requests table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        requester TEXT NOT NULL,
        department TEXT NOT NULL,
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        justification TEXT NOT NULL,
        status TEXT DEFAULT 'PENDING',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Create notifications table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipient TEXT NOT NULL,
        message TEXT NOT NULL,
        request_id INTEGER,
        sent_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (request_id) REFERENCES requests (id)
    )
    ''')
    
    db.commit()
    
    # Insert default users if none exist
    cursor.execute('SELECT COUNT(*) as count FROM users')
    if cursor.fetchone()['count'] == 0:
        default_users = [
            ('ella.weir', 'Emmanuella Nana Ama Weir', 'Staff', 'IT Department'),
            ('dept.head', 'Department Head', 'Department Head', 'IT Department'),
            ('procurement.officer', 'Procurement Officer', 'Procurement Officer', 'Procurement'),
            ('admin', 'System Administrator', 'Admin', 'IT')
        ]
        cursor.executemany(
            'INSERT INTO users (username, full_name, role, department) VALUES (?, ?, ?, ?)',
            default_users
        )
        db.commit()

# ============================================================================
# HTML Templates (Inline for simplicity in prototype)
# ============================================================================

HOME_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Ella's Procurement System - Home</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
        .header { background: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        .header h1 { margin: 0; }
        .header p { margin: 5px 0 0 0; opacity: 0.9; }
        .nav { background: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .nav a { margin-right: 15px; color: #3498db; text-decoration: none; font-weight: bold; }
        .nav a:hover { text-decoration: underline; }
        .card { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .card h2 { margin-top: 0; color: #2c3e50; }
        .stats { display: flex; gap: 15px; flex-wrap: wrap; }
        .stat-box { flex: 1; min-width: 200px; background: #3498db; color: white; padding: 20px; border-radius: 8px; text-align: center; }
        .stat-box h3 { margin: 0; font-size: 2em; }
        .stat-box p { margin: 5px 0 0 0; opacity: 0.9; }
        .request-table { width: 100%; border-collapse: collapse; }
        .request-table th { background: #34495e; color: white; padding: 12px; text-align: left; }
        .request-table td { padding: 12px; border-bottom: 1px solid #ddd; }
        .request-table tr:hover { background: #f9f9f9; }
        .badge { padding: 4px 8px; border-radius: 4px; font-size: 0.85em; font-weight: bold; }
        .badge-pending { background: #f39c12; color: white; }
        .badge-approved { background: #27ae60; color: white; }
        .badge-rejected { background: #e74c3c; color: white; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🏥 Ella's Procurement System</h1>
        <p>Korle-Bu Teaching Hospital - IT Department</p>
    </div>
    
    <div class="nav">
        <a href="/">🏠 Home</a>
        <a href="/create_request">➕ New Request</a>
        <a href="/admin">👤 Admin Panel</a>
        <a href="/register_user">📝 Register User</a>
    </div>
    
    <div class="card">
        <h2>📊 System Statistics</h2>
        <div class="stats">
            <div class="stat-box">
                <h3>{{ stats.total }}</h3>
                <p>Total Requests</p>
            </div>
            <div class="stat-box" style="background: #f39c12;">
                <h3>{{ stats.pending }}</h3>
                <p>Pending</p>
            </div>
            <div class="stat-box" style="background: #27ae60;">
                <h3>{{ stats.approved }}</h3>
                <p>Approved</p>
            </div>
            <div class="stat-box" style="background: #e74c3c;">
                <h3>{{ stats.rejected }}</h3>
                <p>Rejected</p>
            </div>
        </div>
    </div>
    
    <div class="card">
        <h2>📋 Recent Procurement Requests</h2>
        {% if requests %}
        <table class="request-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Requester</th>
                    <th>Department</th>
                    <th>Item</th>
                    <th>Quantity</th>
                    <th>Status</th>
                    <th>Created</th>
                </tr>
            </thead>
            <tbody>
                {% for req in requests %}
                <tr>
                    <td>#{{ req.id }}</td>
                    <td>{{ req.requester }}</td>
                    <td>{{ req.department }}</td>
                    <td>{{ req.item_name }}</td>
                    <td>{{ req.quantity }}</td>
                    <td>
                        <span class="badge badge-{{ req.status|lower }}">{{ req.status }}</span>
                    </td>
                    <td>{{ req.created_at[:10] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p>No requests found. <a href="/create_request">Create your first request</a>.</p>
        {% endif %}
    </div>
    
    <div class="card">
        <h2>ℹ️ About This Prototype</h2>
        <p>This is a minimal Flask-based prototype demonstrating the procurement request workflow for Korle-Bu Teaching Hospital.</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li>Submit procurement requests with item details and justification</li>
            <li>Track request status (Pending, Approved, Rejected)</li>
            <li>User registration with role-based access</li>
            <li>Simple notification system</li>
            <li>Admin panel for managing requests and users</li>
        </ul>
        <p><strong>Note:</strong> This is for demonstration purposes only. Production system should implement proper authentication, authorization, and security measures as outlined in the field trip report.</p>
    </div>
</body>
</html>
'''

CREATE_REQUEST_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Create Procurement Request</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
        .header { background: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        .header h1 { margin: 0; }
        .nav { background: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .nav a { margin-right: 15px; color: #3498db; text-decoration: none; font-weight: bold; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: bold; color: #2c3e50; }
        .form-group input, .form-group select, .form-group textarea { 
            width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; box-sizing: border-box;
        }
        .form-group textarea { min-height: 100px; }
        .btn { background: #3498db; color: white; padding: 12px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        .btn:hover { background: #2980b9; }
        .success { background: #d4edda; border: 1px solid #c3e6cb; color: #155724; padding: 15px; border-radius: 4px; margin-bottom: 20px; }
        .error { background: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; padding: 15px; border-radius: 4px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>➕ Create Procurement Request</h1>
    </div>
    
    <div class="nav">
        <a href="/">🏠 Home</a>
        <a href="/create_request">➕ New Request</a>
        <a href="/admin">👤 Admin Panel</a>
    </div>
    
    <div class="card">
        <form method="POST" action="/create_request">
            <div class="form-group">
                <label for="requester">Requester Name:</label>
                <input type="text" id="requester" name="requester" required placeholder="Your full name">
            </div>
            
            <div class="form-group">
                <label for="department">Department:</label>
                <select id="department" name="department" required>
                    <option value="">Select department...</option>
                    <option value="IT Department">IT Department</option>
                    <option value="Cardiology">Cardiology</option>
                    <option value="Surgery">Surgery</option>
                    <option value="Pediatrics">Pediatrics</option>
                    <option value="Radiology">Radiology</option>
                    <option value="Laboratory">Laboratory</option>
                    <option value="Pharmacy">Pharmacy</option>
                    <option value="Emergency">Emergency</option>
                    <option value="Administration">Administration</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="item_name">Item Name:</label>
                <input type="text" id="item_name" name="item_name" required placeholder="e.g., Dell Latitude 5420 Laptop">
            </div>
            
            <div class="form-group">
                <label for="quantity">Quantity:</label>
                <input type="number" id="quantity" name="quantity" required min="1" value="1">
            </div>
            
            <div class="form-group">
                <label for="justification">Justification:</label>
                <textarea id="justification" name="justification" required placeholder="Explain why this item is needed and how it will be used..."></textarea>
            </div>
            
            <button type="submit" class="btn">Submit Request</button>
        </form>
    </div>
</body>
</html>
'''

ADMIN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Admin Panel</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
        .header { background: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        .header h1 { margin: 0; }
        .nav { background: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .nav a { margin-right: 15px; color: #3498db; text-decoration: none; font-weight: bold; }
        .card { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .card h2 { margin-top: 0; color: #2c3e50; }
        table { width: 100%; border-collapse: collapse; }
        th { background: #34495e; color: white; padding: 12px; text-align: left; }
        td { padding: 12px; border-bottom: 1px solid #ddd; }
        tr:hover { background: #f9f9f9; }
        .badge { padding: 4px 8px; border-radius: 4px; font-size: 0.85em; font-weight: bold; }
        .badge-staff { background: #3498db; color: white; }
        .badge-department.head { background: #9b59b6; color: white; }
        .badge-procurement.officer { background: #e67e22; color: white; }
        .badge-admin { background: #e74c3c; color: white; }
    </style>
</head>
<body>
    <div class="header">
        <h1>👤 Admin Panel</h1>
    </div>
    
    <div class="nav">
        <a href="/">🏠 Home</a>
        <a href="/create_request">➕ New Request</a>
        <a href="/admin">👤 Admin Panel</a>
        <a href="/register_user">📝 Register User</a>
    </div>
    
    <div class="card">
        <h2>👥 Registered Users</h2>
        {% if users %}
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Username</th>
                    <th>Full Name</th>
                    <th>Role</th>
                    <th>Department</th>
                    <th>Registered</th>
                </tr>
            </thead>
            <tbody>
                {% for user in users %}
                <tr>
                    <td>{{ user.id }}</td>
                    <td>{{ user.username }}</td>
                    <td>{{ user.full_name }}</td>
                    <td><span class="badge badge-{{ user.role|lower|replace(' ', '.') }}">{{ user.role }}</span></td>
                    <td>{{ user.department or 'N/A' }}</td>
                    <td>{{ user.created_at[:10] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p>No users registered yet.</p>
        {% endif %}
    </div>
    
    <div class="card">
        <h2>📋 All Procurement Requests</h2>
        {% if requests %}
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Requester</th>
                    <th>Department</th>
                    <th>Item</th>
                    <th>Qty</th>
                    <th>Status</th>
                    <th>Created</th>
                </tr>
            </thead>
            <tbody>
                {% for req in requests %}
                <tr>
                    <td>#{{ req.id }}</td>
                    <td>{{ req.requester }}</td>
                    <td>{{ req.department }}</td>
                    <td>{{ req.item_name }}</td>
                    <td>{{ req.quantity }}</td>
                    <td><span class="badge badge-{{ req.status|lower }}">{{ req.status }}</span></td>
                    <td>{{ req.created_at[:10] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p>No requests in system.</p>
        {% endif %}
    </div>
    
    <div class="card">
        <h2>📬 Recent Notifications</h2>
        {% if notifications %}
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Recipient</th>
                    <th>Message</th>
                    <th>Request ID</th>
                    <th>Sent At</th>
                </tr>
            </thead>
            <tbody>
                {% for notif in notifications %}
                <tr>
                    <td>{{ notif.id }}</td>
                    <td>{{ notif.recipient }}</td>
                    <td>{{ notif.message }}</td>
                    <td>{{ notif.request_id or 'N/A' }}</td>
                    <td>{{ notif.sent_at[:19] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p>No notifications sent yet.</p>
        {% endif %}
    </div>
</body>
</html>
'''

REGISTER_USER_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Register User</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
        .header { background: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        .header h1 { margin: 0; }
        .nav { background: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .nav a { margin-right: 15px; color: #3498db; text-decoration: none; font-weight: bold; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: bold; color: #2c3e50; }
        .form-group input, .form-group select { 
            width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; box-sizing: border-box;
        }
        .btn { background: #27ae60; color: white; padding: 12px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        .btn:hover { background: #229954; }
        .success { background: #d4edda; border: 1px solid #c3e6cb; color: #155724; padding: 15px; border-radius: 4px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>📝 Register New User</h1>
    </div>
    
    <div class="nav">
        <a href="/">🏠 Home</a>
        <a href="/create_request">➕ New Request</a>
        <a href="/admin">👤 Admin Panel</a>
        <a href="/register_user">📝 Register User</a>
    </div>
    
    <div class="card">
        <form method="POST" action="/register_user">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required placeholder="e.g., ella.weir">
            </div>
            
            <div class="form-group">
                <label for="full_name">Full Name:</label>
                <input type="text" id="full_name" name="full_name" required placeholder="e.g., Emmanuella Nana Ama Weir">
            </div>
            
            <div class="form-group">
                <label for="role">Role:</label>
                <select id="role" name="role" required>
                    <option value="">Select role...</option>
                    <option value="Staff">Staff</option>
                    <option value="Department Head">Department Head</option>
                    <option value="Procurement Officer">Procurement Officer</option>
                    <option value="Admin">Admin</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="department">Department:</label>
                <select id="department" name="department">
                    <option value="">Select department (optional)...</option>
                    <option value="IT Department">IT Department</option>
                    <option value="Cardiology">Cardiology</option>
                    <option value="Surgery">Surgery</option>
                    <option value="Pediatrics">Pediatrics</option>
                    <option value="Radiology">Radiology</option>
                    <option value="Laboratory">Laboratory</option>
                    <option value="Pharmacy">Pharmacy</option>
                    <option value="Emergency">Emergency</option>
                    <option value="Administration">Administration</option>
                    <option value="Procurement">Procurement</option>
                </select>
            </div>
            
            <button type="submit" class="btn">Register User</button>
        </form>
    </div>
</body>
</html>
'''

SIMULATE_SEND_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Simulate Notification</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
        .header { background: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        .header h1 { margin: 0; }
        .nav { background: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .nav a { margin-right: 15px; color: #3498db; text-decoration: none; font-weight: bold; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: bold; color: #2c3e50; }
        .form-group input, .form-group select, .form-group textarea { 
            width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; box-sizing: border-box;
        }
        .btn { background: #e67e22; color: white; padding: 12px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        .btn:hover { background: #d35400; }
    </style>
</head>
<body>
    <div class="header">
        <h1>📧 Simulate Notification Send</h1>
    </div>
    
    <div class="nav">
        <a href="/">🏠 Home</a>
        <a href="/admin">👤 Admin Panel</a>
        <a href="/simulate_send">📧 Simulate Send</a>
    </div>
    
    <div class="card">
        <p>Use this tool to simulate sending a notification to a user about a procurement request.</p>
        <form method="POST" action="/simulate_send">
            <div class="form-group">
                <label for="recipient">Recipient:</label>
                <input type="text" id="recipient" name="recipient" required placeholder="e.g., dept.head">
            </div>
            
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" required style="min-height: 100px;" placeholder="Notification message..."></textarea>
            </div>
            
            <div class="form-group">
                <label for="request_id">Request ID (optional):</label>
                <input type="number" id="request_id" name="request_id" placeholder="e.g., 1">
            </div>
            
            <button type="submit" class="btn">Send Notification</button>
        </form>
    </div>
</body>
</html>
'''

SUCCESS_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
    <meta http-equiv="refresh" content="3;url={{ redirect_url }}">
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; background: #f5f5f5; }
        .success-card { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; }
        .success-icon { font-size: 64px; color: #27ae60; }
        h1 { color: #2c3e50; }
        p { color: #7f8c8d; }
        a { color: #3498db; text-decoration: none; }
    </style>
</head>
<body>
    <div class="success-card">
        <div class="success-icon">✓</div>
        <h1>{{ message }}</h1>
        <p>Redirecting you back in 3 seconds...</p>
        <p>Or click <a href="{{ redirect_url }}">here</a> to go back now.</p>
    </div>
</body>
</html>
'''

# ============================================================================
# Routes
# ============================================================================

@app.route('/')
def home():
    """Home page showing system statistics and recent requests"""
    db = get_db()
    
    # Get statistics
    cursor = db.execute('SELECT COUNT(*) as total FROM requests')
    total = cursor.fetchone()['total']
    
    cursor = db.execute("SELECT COUNT(*) as count FROM requests WHERE status = 'PENDING'")
    pending = cursor.fetchone()['count']
    
    cursor = db.execute("SELECT COUNT(*) as count FROM requests WHERE status = 'APPROVED'")
    approved = cursor.fetchone()['count']
    
    cursor = db.execute("SELECT COUNT(*) as count FROM requests WHERE status = 'REJECTED'")
    rejected = cursor.fetchone()['count']
    
    stats = {
        'total': total,
        'pending': pending,
        'approved': approved,
        'rejected': rejected
    }
    
    # Get recent requests
    cursor = db.execute('SELECT * FROM requests ORDER BY created_at DESC LIMIT 10')
    requests = cursor.fetchall()
    
    return render_template_string(HOME_TEMPLATE, stats=stats, requests=requests)

@app.route('/admin')
def admin():
    """Admin panel showing all users, requests, and notifications"""
    db = get_db()
    
    # Get all users
    cursor = db.execute('SELECT * FROM users ORDER BY created_at DESC')
    users = cursor.fetchall()
    
    # Get all requests
    cursor = db.execute('SELECT * FROM requests ORDER BY created_at DESC')
    requests = cursor.fetchall()
    
    # Get recent notifications
    cursor = db.execute('SELECT * FROM notifications ORDER BY sent_at DESC LIMIT 20')
    notifications = cursor.fetchall()
    
    return render_template_string(ADMIN_TEMPLATE, users=users, requests=requests, notifications=notifications)

@app.route('/create_request', methods=['GET', 'POST'])
def create_request():
    """Create a new procurement request"""
    if request.method == 'POST':
        # Get form data
        requester = request.form.get('requester')
        department = request.form.get('department')
        item_name = request.form.get('item_name')
        quantity = request.form.get('quantity')
        justification = request.form.get('justification')
        
        # Validate required fields
        if not all([requester, department, item_name, quantity, justification]):
            return "Missing required fields", 400
        
        # Insert into database
        db = get_db()
        cursor = db.execute(
            '''INSERT INTO requests (requester, department, item_name, quantity, justification, status)
               VALUES (?, ?, ?, ?, ?, 'PENDING')''',
            (requester, department, item_name, int(quantity), justification)
        )
        db.commit()
        request_id = cursor.lastrowid
        
        # Create notification for department head
        db.execute(
            '''INSERT INTO notifications (recipient, message, request_id)
               VALUES (?, ?, ?)''',
            ('dept.head', f'New procurement request #{request_id} from {requester} for {item_name}', request_id)
        )
        db.commit()
        
        return render_template_string(SUCCESS_TEMPLATE, 
                                     message=f'Request #{request_id} created successfully!',
                                     redirect_url='/')
    
    return render_template_string(CREATE_REQUEST_TEMPLATE)

@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    """Register a new user"""
    if request.method == 'POST':
        username = request.form.get('username')
        full_name = request.form.get('full_name')
        role = request.form.get('role')
        department = request.form.get('department')
        
        if not all([username, full_name, role]):
            return "Missing required fields", 400
        
        db = get_db()
        try:
            db.execute(
                'INSERT INTO users (username, full_name, role, department) VALUES (?, ?, ?, ?)',
                (username, full_name, role, department)
            )
            db.commit()
            return render_template_string(SUCCESS_TEMPLATE,
                                         message=f'User {username} registered successfully!',
                                         redirect_url='/admin')
        except sqlite3.IntegrityError:
            return "Username already exists", 400
    
    return render_template_string(REGISTER_USER_TEMPLATE)

@app.route('/simulate_send', methods=['GET', 'POST'])
def simulate_send():
    """Simulate sending a notification"""
    if request.method == 'POST':
        recipient = request.form.get('recipient')
        message = request.form.get('message')
        request_id = request.form.get('request_id')
        
        if not all([recipient, message]):
            return "Missing required fields", 400
        
        db = get_db()
        db.execute(
            'INSERT INTO notifications (recipient, message, request_id) VALUES (?, ?, ?)',
            (recipient, message, int(request_id) if request_id else None)
        )
        db.commit()
        
        return render_template_string(SUCCESS_TEMPLATE,
                                     message='Notification sent successfully!',
                                     redirect_url='/admin')
    
    return render_template_string(SIMULATE_SEND_TEMPLATE)

# ============================================================================
# API Endpoints (JSON responses for external integration)
# ============================================================================

@app.route('/api/requests', methods=['GET'])
def api_list_requests():
    """API endpoint to list all requests as JSON"""
    db = get_db()
    cursor = db.execute('SELECT * FROM requests ORDER BY created_at DESC')
    rows = cursor.fetchall()
    return jsonify([dict(row) for row in rows])

@app.route('/api/requests/<int:request_id>', methods=['GET'])
def api_get_request(request_id):
    """API endpoint to get a specific request"""
    db = get_db()
    cursor = db.execute('SELECT * FROM requests WHERE id = ?', (request_id,))
    row = cursor.fetchone()
    if row:
        return jsonify(dict(row))
    return jsonify({'error': 'Request not found'}), 404

@app.route('/api/users', methods=['GET'])
def api_list_users():
    """API endpoint to list all users as JSON"""
    db = get_db()
    cursor = db.execute('SELECT * FROM users ORDER BY created_at DESC')
    rows = cursor.fetchall()
    return jsonify([dict(row) for row in rows])

# ============================================================================
# Application Entry Point
# ============================================================================

if __name__ == '__main__':
    # Initialize database on startup
    with app.app_context():
        init_db()
        print("✓ Database initialized: ella.db")
        print("✓ Default users created")
        print("\n" + "="*60)
        print("🏥 Ella's Procurement System Prototype")
        print("="*60)
        print("Server starting on http://127.0.0.1:5000")
        print("\nAvailable routes:")
        print("  • http://127.0.0.1:5000/           - Home page")
        print("  • http://127.0.0.1:5000/admin      - Admin panel")
        print("  • http://127.0.0.1:5000/create_request - Create request")
        print("  • http://127.0.0.1:5000/register_user  - Register user")
        print("  • http://127.0.0.1:5000/simulate_send  - Send notification")
        print("\nAPI endpoints:")
        print("  • GET /api/requests - List all requests")
        print("  • GET /api/requests/<id> - Get specific request")
        print("  • GET /api/users - List all users")
        print("="*60 + "\n")
    
    # Run the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True)
