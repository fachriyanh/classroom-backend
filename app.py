from flask import Flask, json, jsonify, request
import os

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def testConnection():
    return 'connected'

@app.route('/register', methods=['POST']) 
def register () :
    body = request.json #membaca input di body
    userData = []
    
    if os.path.exists('./user-file.json') : 
        userFile = open('./user-file.json','r')
        userData = json.load(userFile)

    for user in userData :
        if body['username'] == user['username'] :
            return 'Username sudah dipakai'
    
    userData.append(body)
    userFile = open('./user-file.json','w')
    userFile.write(json.dumps(userData))

    return jsonify(body)


@app.route('/login', methods=['POST'])
def login () :
    body = request.json

    userFile = open('./user-file.json','r')
    userData = json.load(userFile) #merubah ke format json

    if body['user'] == userData['user'] :
        if body['pass'] == userData['pass'] :
            return 'Login Berhasil'
        else :
            return 'Password anda salah'
    else :
        return 'User tidak ditemukan'

@app.route('/user')
def user () :
    userFile = open('./user-file.json','r')
    userData = json.load(userFile)
    return jsonify(userData)

@app.route('/users/<int:id>', methods=["GET"])
def getUser(id):
    # siapin file buat di read
    userFile = open('./users-file.json', 'r')
    userData = json.load(userFile)

    for user in userData:
        if id == user["userid"]:
            return jsonify(user)

    return "User ID {} is not found".format(id)

@app.route('/class',methods = ['POST'])
def createClass () :
    body = request.json #membaca input di body
    userFile = open('./class-file.json','w') #menulis di file json
    userFile.write(json.dumps(body)) #disimpan dalam format json agar bisa dibaca lagi (json pakai dua petik)
    return jsonify(body)

@app.route('/classes', methods=["GET"])
def getAllClasses():

    classesFile = open('./classes-file.json', 'r')
    classesData = json.load(classesFile)

    return jsonify(classesData)

