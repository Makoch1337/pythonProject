import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Получаем параметры подключения из переменных окружения
db_host = os.getenv("DATABASE_HOST", "localhost")
db_port = os.getenv("DATABASE_PORT", "5432")
db_user = os.getenv("DATABASE_USER", "postgres")
db_password = os.getenv("DATABASE_PASSWORD", "admin")
db_name = os.getenv("DATABASE_NAME", "flaskdb")

# Подключение к базе данных
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    user="postgres",
    password="admin",
    dbname=db_name
)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    return jsonify({"response": f"Your message: {message}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
