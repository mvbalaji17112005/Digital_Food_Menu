from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Atlas URI
client = MongoClient("mongodb+srv://Balaji:22BCB7289@cluster0.2avlt7z.mongodb.net/")
db = client["Menu"]
foods = db["foods"]

@app.route('/')
def index():
    all_foods = list(foods.find())
    return render_template('index.html', foods=all_foods)

@app.route('/add', methods=['GET', 'POST'])
def add_food():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        category = request.form['category']
        type_ = request.form['type']
        foods.insert_one({
            'name': name,
            'price': price,
            'category': category,
            'type': type_
        })
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<food_id>', methods=['GET', 'POST'])
def edit_food(food_id):
    food = foods.find_one({'_id': ObjectId(food_id)})
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        category = request.form['category']
        type_ = request.form['type']
        foods.update_one({'_id': ObjectId(food_id)}, {
            '$set': {
                'name': name,
                'price': price,
                'category': category,
                'type': type_
            }
        })
        return redirect(url_for('index'))
    return render_template('edit.html', food=food)

@app.route('/delete/<food_id>')
def delete_food(food_id):
    foods.delete_one({'_id': ObjectId(food_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
