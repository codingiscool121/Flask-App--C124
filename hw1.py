from flask import Flask, app, jsonify, request

app=Flask(__name__)


contacts= [
    {
        "Contact": "860508918",
        "id":1
    },
    {
        "Contact": "869008918",
        "id":2
    },
    {
        "Contact": "98765421",
        "id":3
    },
    {
        "Contact": "1391293",
        "id":4
    },
    {
        "Contact": "123456789",
        "id":5
    },
    {
        "Contact": "987654",
        "id":6
    },
    {
        "Contact": "987654",
        "id":7
    },
]

@ app.route('/')
def home():
    return "Welcome to the home page. Let's take a look at some contacts."

@app.route('/sendinfo', methods=['POST'])
def sendinfo():
    if not request.json:
        return jsonify({'status':'Error', 'Message':'Invalid Data'}, 400)
    temp = {
        'id': contacts[-1]['id'] + 1,
        'Contact': request.json['Contact'],
    }
    contacts.append(temp)
    return jsonify({'status':'Success', 'Message':'Data Added'}, 201)

@app.route('/getinfo', methods=['GET'])
def getinfo():
    return jsonify({'data': contacts})



#If the main process is running, then it will run the app.
if __name__ == '__main__':
    app.run(debug=True)