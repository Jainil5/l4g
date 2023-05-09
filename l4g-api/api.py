import openai
import requests
from flask import Flask
from flask_restful import Api,Resource

openai.api_key = "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"

app = Flask(__name__)
api = Api(app)


schema = {
            "accounts":["id","name","ownerID","ofClientsYears","activeProgramCohort","programCohortHistory","alternateAccountName","annualBudgetMostRecent","billingAddressCity"],
            "applications":["id","name","ofClientsYears","accountId","annualActualBudget","budgetRangeCalc","ediApproach","fullTimeStaffCount","fullTimeStaffRange","headOfOrgRaceEthnicity"]
}

messages = []

messages.append({"role":"user","content":str(schema)})

def ask(input):    
    text = str(input).lower().strip()
    messages.append({"role":"user","content":text})
    response = openai.ChatCompletion.create(model= "gpt-3.5-turbo",messages = messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant" , "content":"reply"})
    print("\n"+reply+"\n")
    return reply


class Update(Resource):
    def post(self,data):
        response = ask(str(data))
        return {data : response}

api.add_resource(Update,"/query/<string:data>")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
    




#   in table accounts A query for names where billing city is surat, bipoc head is Modi and active program cohort is 0.
#   A query for id where anual budget greater than lakh , orgaization type is sevice an sponsor is jio.
#  in applications a query to find id where client years > 2 