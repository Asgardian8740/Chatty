from flask import Flask, request , make_response
import json

app = Flask(__name__)

dummy_data = {
    "weight" : 70,
    "height" : 164,
    "BMI" : 30
}

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/webhook' , methods=["POST"])
def webhook():

    if (request.method == "POST"):
        req = request.get_json(silent=True , force = True)
        res = processRequest(req)

        res = json.dumps(res,indent =4)
        r = make_response(res)
        #r.header['Content-Type'] = 'application/json'
        return r



def processRequest(req):

    #get all the query parameter
    query_res = req["queryResult"]
    print(query_res)
    text = query_res.get('queryText' , None)
    parameters = query_res.get('parameters' , None)
    res = get_data()
    return res

def get_data():

    name = "shakya"
    return {"fulfillmentText": name,}

if __name__ == '__main__':
    app.run(debug=True)
