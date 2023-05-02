import openai
import requests
from flask import Flask
from flask_restful import Api,Resource

openai.api_key = "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"
app = Flask(__name__)
api = Api(app)

def query_for(x):
    global input
    input = {
            "accounts":["id","name","ownerID","ofClientsYears","activeProgramCohort","programCohortHistory","alternateAccountName","annualBudgetMostRecent","billingAddressCity"],
            "applications":["id","name","ofClientsYears","accountId","annualActualBudget","budgetRangeCalc","ediApproach","fullTimeStaffCount","fullTimeStaffRange","headOfOrgRaceEthnicity"]
    }
    messages = []
    first="Table "
    schema = input.json()
    gen = str(x).index("generate")
    for i in schema:
        if i in x[:gen]:
            first = first+i
            first = first +"with properties:" +str(schema[i])
        #else'
    messages.append({"role": "user", "content": first})
    messages.append({"role":"user","content":x})
    response = openai.ChatCompletion.create(model= "gpt-3.5-turbo",messages = messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant" , "content":"reply"})
    print("\n"+reply+"\n")
    return reply

class Update(Resource):
    def get(self,data):
        response = query_for(str(data))
        return {data : response}

api.add_resource(Update,"/query/<string:data>")

if __name__ == "__main__":
    app.run(debug=True,port=5000)



#   A query for names where billing city is surat, bipoc head is Modi and active program cohort is 0.
#   A query for id where anual budget greater than lakh , orgaization type is sevice an sponsor is jio.