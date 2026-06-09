from flask import Flask, render_template, request

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

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form.get('username')
    email = request.form.get('email')
    from db import get_db_connection
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mytable (name, email) VALUES (%s, %s)', (username, email))
    conn.commit()
    cursor.close()
    conn.close()
    return 'User created successfully!'