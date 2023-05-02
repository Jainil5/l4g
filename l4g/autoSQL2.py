import os
import openai
import csv

openai.api_key = "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"

def get_fields(x):
    with open(x,"r") as file:
        reader = csv.reader(file)
        fields = next(reader)
        return fields
def Query(x):
    list = get_fields("SFAccounts.csv")
    default = "SQL table, with their properties: L4G"+str(list)
    ask = default + str(x)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ask}])
    print(str("\nQuery: " + x + "\n\n" + completion["choices"][0]["message"]["content"] + "\n"))


Query("A query to list the items with billing city surat and mrp greater than 1000 and cohort history greater than 5 where bipoc head of org is Modi.")
