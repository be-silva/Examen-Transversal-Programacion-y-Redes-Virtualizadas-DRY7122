import pyotp
import sqlite3
import hashlib
import uuid

from flask import Flask, request
app = Flask(__name__)

db_name = 'test.db'

@app.route('/')
def index():
    return 'EXAMEN TRANSVERSAL DRY7122'


@app.route('/registro/ET', methods=['GET', 'POST'])
def signup_v2():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,
            HASH      TEXT    NOT NULL);''')
    conn.commit()
    try:
        hash_value = hashlib.sha256(request.form['password'].encode()).hexdigest()
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) "
                  "VALUES ('{0}', '{1}')".format(request.form['username'], hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return "Usuario ya registrado."
    print('username: ', request.form['username'], ' password: ', request.form['password'], ' hash: ', hash_value)
    return "Registro Exitoso"


def verify_hash(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == hashlib.sha256(password.encode()).hexdigest()



@app.route('/ingreso/ET', methods=['GET', 'POST'])
def login_v2():
    error = None
    if request.method == 'POST':
        if verify_hash(request.form['username'], request.form['password']):
            error = 'Ingreso exitoso!'
        else:
            error = 'Usuario o Contraseña inválidos'
    else:
        error = 'Método Inválido.'
    return error




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800, ssl_context='adhoc')