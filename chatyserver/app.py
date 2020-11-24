from flask import Flask, request , make_response
import json
from user import *
from doctor import *

app = Flask(__name__)


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
    print(req.keys())
    if(req.get("queryResult").get("intent").get("displayName") == "logIn"):
        return loginintent()

    if (req.get("queryResult").get("intent").get("displayName") == "Recent_lab_report"):
        return labreportintent()

    if (req.get("queryResult").get("intent").get("displayName") == "nearest_doctor"):
        return doctor_intent()

    if (req.get("queryResult").get("intent").get("displayName") == "prescriptions"):
        return presc_intent()

    if (req.get("queryResult").get("intent").get("displayName") == "med_store"):
        return medstore_intent()

    if (req.get("queryResult").get("intent").get("displayName") == "Pat_health_stat"):
        return pathealth_intent()

    if (req.get("queryResult").get("intent").get("displayName") == "Pat_medication"):
        return patmed_intent()

    if (req.get("queryResult").get("intent").get("displayName") == "Pat_med_date"):
        return patmeddate_intent()

    if (req.get("queryResult").get("intent").get("displayName") == "Pat_imun"):
        return patimun_intent()

    if (req.get("queryResult").get("intent").get("displayName") == "pat_Imun_date"):
        return patimundate_intent()

    if (req.get("queryResult").get("intent").get("displayName") == "pat_lab_code"):
        return patlabcode_intent()

    if (req.get("queryResult").get("intent").get("displayName") == "pat_stat_nut"):
        return patstatnut_intent()





    #get all the query parameter
    query_res = req["queryResult"]
    print(query_res)
    return get_data("Please return user Id")

def get_data(data):
    return {"fulfillmentText": data}


if __name__ == '__main__':
    app.run(debug=True)
