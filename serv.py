from flask import Flask, jsonify, request, abort
import requests, os, signal

app = Flask(__name__)

data = ''


def calculate(jsn):
    jsn_out = {
        'SumResult': 0,
        'MulResult': 1,
        'SortedInputs': []
    }
    k = jsn['K']
    sum = 0
    for el in jsn['Sums']:
        sum += el
        jsn_out['SortedInputs'].append(el)

    jsn_out['SumResult'] = round(sum * k, 2)

    for el in jsn['Muls']:
        jsn_out['MulResult'] *= el
        jsn_out['SortedInputs'].append(el)

    jsn_out['SortedInputs'].sort()
    return jsn_out


@app.route('/')
def index():
    return ''


@app.route('/Ping')
def ping():
    res = requests.get('http://127.0.0.1:5000/')
    if res.status_code == 200:
        return jsonify(res.status_code)
    else:
        return abort(400)


@app.route('/PostInputData', methods=['POST'])
def post_input_data():
    # curl --request POST --header 'Content-Type: application/json' --data '{"K":10,"Sums":[1.01,2.02],"Muls":[1,4]}' 'http://127.0.0.1:5000/PostInputData'
    #     {"K":10,"Sums":[1.01,2.02],"Muls":[1,4]}
    global data
    data = request.get_json(force=True)
    print(data)
    return jsonify(data)


@app.route('/GetAnswer')
def get_answer():
    print(data)
    print(calculate(data))
    return jsonify(calculate(data))


@app.route('/Stop')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({"success": True, "message": "Server is shutting down..."})


if __name__ == '__main__':
    app.run(debug=True)
