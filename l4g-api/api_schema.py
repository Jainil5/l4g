from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class schema(Resource):
    def get(self):
        return {
            "accounts":["id","name","ownerID","ofClientsYears","activeProgramCohort","programCohortHistory","alternateAccountName","annualBudgetMostRecent","billingAddressCity"],
            "applications":["id","name","ofClientsYears","accountId","annualActualBudget","budgetRangeCalc","ediApproach","fullTimeStaffCount","fullTimeStaffRange","headOfOrgRaceEthnicity"]
        }

api.add_resource(schema,"/schema")

if __name__ == "__main__":
    app.run(debug=True,port=2000)