from app import app
from flask import render_template, request, Response, redirect, session
from auto import predict
import base64
import face
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/select', methods=['GET', 'POST'])
def select():
    price = ''
    if request.method == 'POST':
        price = predict(request.form)
    else:
        print 'get'
    return render_template('select.html', price = price, name = session['name'])

@app.route('/saveImage', methods=['GET', 'POST'])
def saveImage():
    name = request.form['name'];
    personId = face.createPerson(name)
    data = base64.decodestring(request.form['data'])

    d = 'images/' + str(personId) +'.png'
    img = open(d, 'w')
    img.write(data)
    img.close()
    face.addFace(personId)
    face.trainGroup()
    return 'ok'

@app.route('/checkImage', methods=['GET', 'POST'])
def checkImage():
    data = base64.decodestring(request.form['data'])
    d = 'images/tmp.png'
    img = open(d, 'w')
    img.write(data)
    img.close()
    name = face.checkFace()
    if name == None:
        return 'no-body-match'
    session['name'] = name
    return name

@app.route('/image/<personId>')
def getImage(personId):
   # personId = '9a900cac-390c-4992-915f-e73473b8b606'
    image = file('images/' + str(personId) + '.png')
    res = Response(image, mimetype='image/png')
    return res