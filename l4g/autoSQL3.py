import csv
import os
from os import listdir
import openai

def get_fields(x):
    with open(x,"r") as file:
        reader = csv.reader(file)
        fields = next(reader)
        return fields

def Query(x):
    openai.api_key = "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"

    pre = "Tables with their properties:"

    selected_list = []
    fields = {}
    folder = "csvs/"
    match = []

    for files in listdir(folder):
        match.append(files[:files.index(".")])
        fields.update({files[:files.index(".")]: get_fields(folder + files)})
    print(fields)

    print(x[3:x.index("")])
    for i in fields.keys():
        if i.lower() in x.lower():
            print("Selected:",i)
            selected_list = fields[i]

    print(selected_list)
    if len(selected_list)!= 0:
        pre += str(selected_list)
        index = x.index("query")
        index -= 1
        ask = pre + str(selected_list) + x[index]
        print(ask)
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ask}])
        print("\n\n" + completion["choices"][0]["message"]["content"] + "\n")

input_account = "In SFApplication generate a query where billing city is california , mrp is greater than 100 cohort history is 0 and bipoc head is Modi "
print(Query(input_account))



