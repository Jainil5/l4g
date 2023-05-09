from flask import Flask
from flask_restful import Api,Resource
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
cors = CORS(app)

schema = {
            "accounts":["id","name","ownerID","ofClientsYears","activeProgramCohort","programCohortHistory","alternateAccountName","annualBudgetMostRecent","billingAddressCity"],
            "applications":["id","name","ofClientsYears","accountId","annualActualBudget","budgetRangeCalc","ediApproach","fullTimeStaffCount","fullTimeStaffRange","headOfOrgRaceEthnicity"]
}
def api_call(x):
    return {x:"SELECT id FROM accounts WHERE billingAddressCity = 'Surat' AND annualBudgetMostRecent > 100000 AND ofClientsYears > 2;"}
class Update(Resource):
    def get(self,data):
        response = api_call(str(data))
        return {data : response}
api.add_resource(Update,"/query/<string:data>")
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)