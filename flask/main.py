from flask import Flask
import psycopg2
app = Flask(__name__)

def fib(n):
    a = 0
    b = 1
    if n <= 1:
        return n 
    i = 0 
    while i < n:
        a,b = b,a+b
        i += 1 
     
    return a

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/fib/<int:value>')
def fibbonaci(value):
    output = fib(value)
    conn = connection()
    cur = create_cursor(conn)
    cur.execute("INSERT INTO numbers(value) VALUES(%s)",(str(output),))
    conn.commit()
    cur.close()
    return str(output)
@app.route('/conn')
def test_conn():
    return str(connection().server_version)
def create_cursor(conn):
    return conn.cursor()
def connection():
    return psycopg2.connect(
        host="172.18.0.3",
        database="postgres",
        user="postgres",
        password="zako123"
    )