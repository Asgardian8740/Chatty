dummy_data = {
    "first_name" : "Monica",
    "last_name" : "Geller",
    "weight" : 70,
    "height" : 164,
    "BMI" : 30,
    "age" : 30,
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
        "name" : "Acetaminophen 325 MG Oral Tablet",
        "start": "2012-04-24",
        "end" : "2013-09-16",
    },
    "med_store" : {
        "name" : "apolo care",
        "add" : "330 MOUNT AUBURN STREET",
        "city" : "CAMBRIDGE",
    },
    "imun" : {
        "name" : "Pneumococcal conjugate PCV 13",
        "date" : "2017-11-03",
    },
    "lab" : {
        "code" : "140",
    },
    "allergy" : {
        "name" : "Latex",
        "start" : "25-10-2018",
    },
}




def pathealth_intent():
    data = get_pat_stats()
    return get_data(data)

def patmed_intent():
    data = get_pat_med()
    return get_data(data)

def patmeddate_intent():
    data = get_pat_med_date()
    return get_data(data)

def patimun_intent():
    data = get_pat_imun()
    return get_data(data)

def patimundate_intent():
    data = get_pat_imundate()
    return get_data(data)

def patlabcode_intent():
    data = get_pat_labcode()
    return get_data(data)

def patstatnut_intent():
    data = get_pat_statnut()
    return get_data(data)


def get_pat_labcode():
    ftext = "labcode of patient is {}. \n".format(dummy_data["lab"]["code"])
    return ftext

def get_pat_imundate():
    ftext = "immunization is give to {}. \n".format(dummy_data["imun"]["date"])
    return ftext

def get_pat_imun():
    ftext = " Patient is consuming : {}  immunization. \n".format(dummy_data["imun"]["name"])
    return ftext

def get_pat_med():
    ftext = " Patient is consuming : {}  \n".format(dummy_data["med"]["name"])
    return ftext

def get_pat_med_date():
    ftext = " Patient medication period is  {} to {}  \n".format(dummy_data["med"]["start"] , dummy_data["med"]["end"])
    return ftext


def get_pat_labcode():
    ftext = " Patient name : {}  \n".format(dummy_data["first_name"])
    ftext += "Weight : {} Kg \n".format(dummy_data["weight"])
    ftext += "Height : {} cm \n".format(dummy_data["height"])
    ftext += " BMI : {} \n".format(dummy_data["BMI"])
    ftext += " AGE : {} \n".format(dummy_data["age"])
    ftext += " Patient has {} allergy from {} \n\n".format(dummy_data["allergy"]["name"] , dummy_data["allergy"]["start"])
    ftext += " Patient is taking {} immunization  \n".format(dummy_data["imun"]["name"])
    ftext += " Patient is taking {} medicitaion  \n".format(dummy_data["med"]["name"])
    return ftext


def get_pat_stats():
    ftext = " Patient name : {}  \n".format(dummy_data["first_name"])
    ftext += "Weight : {} Kg \n".format(dummy_data["weight"])
    ftext += "Height : {} cm \n".format(dummy_data["height"])
    ftext += " BMI : {} \n".format(dummy_data["BMI"])
    return ftext

def get_data(data):
    return {"fulfillmentText": data}