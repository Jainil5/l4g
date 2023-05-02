import os
import openai
import csv

openai.api_key = "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"

def get_fields(x):
    with open(x,"r") as file:
        reader = csv.reader(file)
        fields = next(reader)
        return fields
def Query(y,x):
    default = "SQL table, with their properties: "+str(y)
    ask = default + str(x)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ask}])
    print(str("\nQuery: " + x + "\n\n" + completion["choices"][0]["message"]["content"] + "\n"))


account = get_fields("csvs/SFAccounts.csv")
applications = get_fields("csvs/SFApplications.csv")
feedback = get_fields("csvs/SFFeedbackLoops.csv")

Query(account,"A query to list the items with billing city surat and mrp greater than 1000 and cohort history greater than 5 where bipoc head is Modi.")
Query(applications,"A query to list names wit client years >5 annual budget > 10000 and sponsor is AppGambit")