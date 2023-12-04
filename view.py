from flask import Blueprint, flash, json, request, render_template
import pickle

import pandas as pd
views = Blueprint(__name__,"views")
# Load the saved model
model_filename = 'random_forest_model.pkl'
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)
# Define the main route which will land. 
@views.route("/" , methods =["GET","POST"])
def home():
    print()
    if request.method == "POST":
       # getting input with name = fname in HTML form
        data = request.form.to_dict(flat=False)
        custom_data_input_dict =  {
        "InscClaimAmtReimbursed": [request.form.get("InscClaimAmtReimbursed") != None or ''],
        "IPAnnualReimbursementAmt": [request.form.get("IPAnnualReimbursementAmt") != None or ''],
        "IPAnnualDeductibleAmt": [request.form.get("IPAnnualDeductibleAmt") != None or ''],
        "OPAnnualReimbursementAmt": [request.form.get("OPAnnualReimbursementAmt") != None or ''],
        "OPAnnualDeductibleAmt": [request.form.get("OPAnnualDeductibleAmt") != None or ''],
        "Age": [request.form.get("Age") != None or ''],
        "DaysAdmitted": [request.form.get("DaysAdmitted") != None or ''],
        "TotalDiagnosis": [request.form.get("TotalDiagnosis") != None or ''],
        "TotalProcedure": [request.form.get("TotalProcedure") != None or ''],
        "EncounterType": [request.form.get("EncounterType") != None or ''],
        "Gender": [request.form.get("Gender") != None or ''],
        "Race": [request.form.get("Race") != None or ''],
        "RenalDiseaseIndicator": [request.form.get("RenalDiseaseIndicator") != None or ''],
        "IsDead": [request.form.get("IsDead") != None or ''],
        "ChronicCond_Alzheimer": [request.form.get("ChronicCond_Alzheimer") != None or False],
       "ChronicCond_Heartfailure" :  [request.form.get("ChronicCond_Heartfailure") != None or False],
       "ChronicCond_KidneyDisease" :[ request.form.get("ChronicCond_KidneyDisease") != None or False],
       "ChronicCond_Cancer" : [request.form.get("ChronicCond_Cancer") != None or False],
       "ChronicCond_ObstrPulmonary" :[ request.form.get("ChronicCond_ObstrPulmonary") != None or False],
       "ChronicCond_Depression" : [request.form.get("ChronicCond_Depression") != None or False],
       "ChronicCond_Diabetes" : [request.form.get("ChronicCond_Diabetes") != None or False],
       "ChronicCond_IschemicHeart" : [request.form.get("ChronicCond_IschemicHeart") != None or False],
       "ChronicCond_Osteoporasis" : [request.form.get("ChronicCond_Osteoporasis") != None or False],
       "ChronicCond_rheumatoidarthritis" : [request.form.get("ChronicCond_rheumatoidarthritis") != None or False],
       "ChronicCond_stroke" : [request.form.get("ChronicCond_stroke") != None or False]
       }
        print(custom_data_input_dict)
        inputData= pd.DataFrame(custom_data_input_dict)
        print(inputData.columns)
        prediction = loaded_model.predict(inputData)
        print(prediction)
        policy_Status = ''  
        if prediction == 0:
          policy_Status = 'Fraud'
        else:
            policy_Status= 'Not Fraud'
        
        return render_template("index.html", scroll=policy_Status, name=policy_Status)
    return render_template("index.html")
    #  add all the outputs here
# @views.route('/')
# def reload():
#   print(request.form)
#   # Cache.clear()
#   return render_template("index.html",scroll='')
