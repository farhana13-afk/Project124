#1
from flask import Flask,jsonify,request

#2
app = Flask(__name__)

#3
contacts=[
    {
        "id": 1,
        "Name": "Raju",
        "Contact": "9987644456",
        "done": False   
    },
    {
        "id": 2,
        "Name": "Rahul",
        "Contact": "9876543222",
        "done": False  
    }
]

#4
@app.route("/add-data", methods=["POST"])
#5
def add_contacts():
#6
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'Please provide the Data'
        },400)
#7
    contact = {
        'id': contacts[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',""),
        'done': False
    }
#8
    contacts.append(contact)
    return jsonify({
        'status': 'success',
        'message': 'Contact added succesfully!'
    })

@app.route("/get-data")
def get_contacts():
    return jsonify({
        'data': contacts  
    })

if (__name__ == "__main__"):
    app.run(debug = True)
    