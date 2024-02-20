from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

# SQLite database setup
conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'h4rdp455w0rd!')")
conn.commit()

# Login route
@app.route('/')
def index():
    return render_template('login.html')

# Authentication route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Vulnerable SQL query (simulating a login)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        flash('Login successful!', 'success')
        return redirect(url_for('success'))
    else:
        flash('Login failed. Incorrect username or password.', 'error')

    return redirect(url_for('index'))

# Successful login route
@app.route('/2JxOEVMIADRQ5RhFqcO3v3')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
