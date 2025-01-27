from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'mythra'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '777111'
app.config['MYSQL_DB'] = 'airplane_db1'  
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/airplane')
def airplane():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM airplane_details")  
    airplane_info = cur.fetchall()
    cur.close()
    return render_template('airplane.html', airplanes=airplane_info)  

@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    search_term = ''
    if request.method == "POST":
        search_term = request.form['plane_id']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM airplane_details WHERE id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchmany(size=1)
        cur.close()
    return render_template('airplane.html', airplanes=search_results)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        plane_id = request.form['plane_id']
        model = request.form['model']
        manufacturer = request.form['manufacturer']
        capacity = request.form['capacity']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO airplane_details (id, model, manufacturer, capacity) VALUES (%s, %s, %s, %s)", 
                    (plane_id, model, manufacturer, capacity))
        mysql.connection.commit()
        return redirect(url_for('airplane'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM airplane_details WHERE id=%s", (id_data,)) 
    mysql.connection.commit()
    return redirect(url_for('airplane'))

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        plane_id = request.form['plane_id']
        model = request.form['model']
        manufacturer = request.form['manufacturer']
        capacity = request.form['capacity']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE airplane_details SET model=%s, manufacturer=%s, capacity=%s WHERE id=%s", 
                    (model, manufacturer, capacity, plane_id))
        mysql.connection.commit()
        return redirect(url_for('airplane'))