from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/update_posture', methods=['POST'])
def update_posture():
    data = request.get_json()
    # write to posture file 
    with open('posture.txt', 'w') as f:
        f.write(str(data['posture']))

    return jsonify({'message': 'success'})

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')



