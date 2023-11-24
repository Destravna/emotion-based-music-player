from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
from detectEmotion import *
from fer import FER
import cv2

emotionDetector = FER(mtcnn=True)

app = Flask(__name__)
cors = CORS(app)

happy = [
    {
        'name' : 'Pasoori',
        'url' : 'http://localhost:8080/songs/happy/Coke Studio _ Season 14 _ Pasoori _ Ali Sethi x Shae Gill.mp3'
    },
    {
        'name' : 'Higher',
        'url' : 'http://localhost:8080/songs/happy/Shawn Mendes - Higher (Lyric Video).mp3'
    }
]


sad = [
    {
        'name':'Disaster',
        'url': 'http://localhost:8080/songs/sad/Conan Gray - Disaster (Official Lyric Video).mp3'
    },
    {
        'name':'Love Yourself',
        'url':'http://localhost:8080/songs/sad/Justin Bieber - Love Yourself (Lyrics).mp3'
    },
    {
        'name':'Know Me Too Well',
        'url':'http://localhost:8080/songs/sad/New Hope Club - Know Me Too Well (Lyrics) _ I spend my weekends tryna get you off.mp3'
    },
    {
        'name':'New Hope Club',
        'url' : 'http://localhost:8080/songs/sad/New Hope Club - Worse (Lyrics).mp3'
    }
]

neutral = [
    {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    },
     {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    },
    {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    }
]

angry = [
    {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    },
     {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    },
    {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    }
]


disgust = [
    {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    },
     {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    },
    {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    }
]

fear = [
    {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    },
     {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    },
    {
        'name':'New Hope Club',
        'url': 'http://localhost:8080/songs/neutral/New Hope Club - Love Again.mp3'
    },
    {
        'name':'Pagalpan',
        'url': 'http://localhost:8080/songs/neutral/Pagalpan - JalRaj _ Safar _ Official Video _ Latest Original Songs 2021 Hindi.mp3'
    },
    {
        'name': 'telepath.mp3',
        'url': 'http://localhost:8080/songs/neutral/telepath.mp3'
    }
]

@app.route("/")
def hello_world():
    return "<p>dhruv singh</p>"

@app.route('/json', methods=['GET'])
def return_json():
    print('request recieved here bitch')
    if(request.method == 'GET'):
        data = {
            'name' : 'Dhruv',
            'reg' : '20BCI'
        }
        return jsonify(data)


@app.route('/detect', methods=['GET', 'POST'])
def save_file():
    # print('request recieved here bitch')
    if(request.method == 'POST'):
        file = request.files['image']
        # print(file)
        filename = secure_filename(file.filename)
        file_path = os.path.join('user_photos', filename)
        print('filename is ', filename)
        file.save(file_path)
        emotion = detect_emotion(filename=filename, emotionDetector=emotionDetector)
        print(emotion)
        data = {
            'emotion' : emotion['emotion'],
        }
        
        return jsonify(data)


@app.route('/upload', methods=['POST'])
@cross_origin()
def save():
    if(request.method == 'POST'):
        print('got a request here___________________')
        file = request.files['image']
        # print(file)
        filename = secure_filename(file.filename)
        file_path = os.path.join('user_photos', filename)
        print('filename is ', filename)
        file.save(file_path)
        data = {
            'msg': 'image saved'
        }
        return jsonify(data)

@app.route('/getSongList/<emotion>', methods = ['GET'])
def send_list(emotion):
    print("yeh emotion chahiye" + emotion)
    if emotion == "sad":
        data = {
            'songs' : sad
        }
    elif emotion == "happy":
        data = {
            'songs' : happy
        }
    else:
        data = {
            'songs' : neutral
        }
    return data


@app.route('/songs/<folder>/<song>', methods=['GET'])
def send_song(folder, song):
    print("folder _______________" + folder)
    print("song _________________" + song)
    return send_from_directory('songs/' + folder, song)


port_number = 8080

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=port_number)