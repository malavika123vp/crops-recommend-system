from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home page – search box
@app.route('/')
def home():
    return render_template('index.html')

# Search results page
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']

    conn = sqlite3.connect('crops.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, soil, fertilizer, image FROM crops WHERE name LIKE ? OR soil LIKE ?", 
                   ('%' + query + '%', '%' + query + '%'))
    results = cursor.fetchall()
    conn.close()

    return render_template('results.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)