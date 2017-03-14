from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enterNew')
def food():
    return render_template('food.html')

@app.route('/addFood', methods = ['POST'])
def addFood():
    connection =sqlite3.connect('database.db')
    cursor = connection.cursor()

    name = request.form['name']
    calories = request.form['calories']
    cuisine = request.form['cuisine']
    is_vegetarian = request.form['is_vegetarian']
    is_gluten_free = request.form['is_gluten_free']
    print (name, calories, cuisine, is_vegetarian, is_gluten_free)

    try:
        cursor.execute('INSERT INTO foods (name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?,?,?,?,?)', (name, calories, cuisine, is_vegetarian, is_gluten_free))
        connection.commit()
        message = "Successfully inserted data into the database"
    except:
        connection.rollback()
        message = "Error inserting the data"
    finally:
        connection.close()
        return message

@app.route('/favourite')
def favourite():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM foods WHERE name = 'Dylan'")
    favouriteList = cursor.fetchall()
    return jsonify(favouriteList)

app.run(debug = True)
