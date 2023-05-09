
schema = {
            "accounts":["id","name","ownerID","ofClientsYears","activeProgramCohort","programCohortHistory","alternateAccountName","annualBudgetMostRecent","billingAddressCity"],
            "applications":["id","name","ofClientsYears","accountId","annualActualBudget","budgetRangeCalc","ediApproach","fullTimeStaffCount","fullTimeStaffRange","headOfOrgRaceEthnicity"]
}

def find_table(input):
    res = str(input).lower().strip()
    schemas = schema
    gen = res.index("generate")
    for i in schemas:
        if i in res[:gen]:
            props = str(schemas[i])    
            print(props)
    return res

print(find_table("In table accounts generate a query for a in cdj"))