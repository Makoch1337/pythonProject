from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host="db",
    database="mydatabase",
    user="admin",
    password="admin"
)
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')
    cursor.execute("INSERT INTO users (name, message) VALUES (%s, %s)", (name, message))
    conn.commit()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
