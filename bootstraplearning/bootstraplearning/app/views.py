from app import app
from flask import render_template

@app.route('/')
def typography():
    return render_template('typography.html')

@app.route('/t')
def table():
    return render_template('table.html')

@app.route('/i')
def image():
    return render_template('image.html')

@app.route('/c')
@app.route('/c1')
def component1():
    return render_template('component1.html')

@app.route('/c2')
def component2():
    return render_template('component2.html')

@app.route('/c3')
def component3():
    return render_template('component3.html')

@app.route('/c4')
def component4():
    return render_template('component4.html')



