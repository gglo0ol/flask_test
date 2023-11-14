from flask import Flask, render_template
from Random_data import Random_data
import SQLite
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    data = Random_data().get_json()
    my_dict = json.loads(data)
    return render_template('about.html', my_dict=my_dict)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
