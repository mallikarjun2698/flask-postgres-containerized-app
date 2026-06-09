from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_users')
def get_users():
    from db import get_db_connection
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mytable')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('data.html', data=data)

@app.route('/create_user/<name>')
def create_user(name):
    from db import get_db_connection
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mytable (name) VALUES (%s)', (name,))
    conn.commit()
    cursor.close()
    conn.close()
    return 'User created successfully!'