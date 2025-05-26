from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compute', methods=['POST'])
def compute():
    data=request.get_json()
    numbers=data['numbers']
    result=sum(x*x for x in numbers)
    return jsonify({'result':result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)