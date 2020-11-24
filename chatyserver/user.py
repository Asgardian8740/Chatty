

dummy_data = {
    "first_name" : "Monica",
    "last_name" : "Geller",
    "weight" : 70,
    "height" : 164,
    "BMI" : 30,
    "reason" : {
        "desc" : "Acute bronchitis (disorder)",
        "code" : "10509002",
        "advice" : "Respiratory therapy"
    },
    "clinic" : {
        "name" : "Luke Rath",
        "city" : "BOSTON",
        "add" : "1153 CENTRE STREET",
    },
    "med" : {
        "desc" : "Respiratory therapy",
        "name" : "Etonogestrel 68 MG Drug Implant"
    },
    "med_store" : {
        "name" : "apolo care",
        "add" : "330 MOUNT AUBURN STREET",
        "city" : "CAMBRIDGE",
    },

}


def loginintent():
    data = get_user_stats()
    return get_data(data)

def labreportintent():
    data = get_lab_report()
    return get_data(data)

def doctor_intent():
    data = get_doctor()
    return get_data(data)

def presc_intent():
    data = get_prescription()
    return get_data(data)

def medstore_intent():
    data = get_medstore()
    return get_data(data)



def get_medstore():
    ftext = "Nearest Medical Store is {}. ".format(dummy_data["med_store"]["name"])
    ftext += "Its address in {} , {} ".format(dummy_data["med_store"]["add"] , dummy_data["med_store"]["city"])
    return ftext




def get_prescription():
    ftext = "You have have been advised with {} plan".format(dummy_data["med"]["desc"])
    ftext += "You have to make these medicines {}. ".format(dummy_data["med"]["name"])
    return ftext

def get_doctor():
    ftext = "Dr. {} ".format(dummy_data["clinic"]["name"])
    ftext += "available at {}, {}.".format(dummy_data["clinic"]["add"] , dummy_data["clinic"]["city"])
    return ftext

def get_lab_report():
    ftext = "As per your recent diagnosis you have {}.".format(dummy_data["reason"]["desc"])
    ftext += "You have to make these medicines. \n {}".format(dummy_data["med"][""])
    return ftext


def get_user_stats():
    ftext = " Hey {}  your latest health stats \n".format(dummy_data["first_name"])
    ftext += "Weight : {} Kg \n".format(dummy_data["weight"])
    ftext += "Height : {} cm \n".format(dummy_data["height"])
    ftext += " BMI : {} \n".format(dummy_data["BMI"])

    return ftext


def get_data(data):
    return {"fulfillmentText": data}