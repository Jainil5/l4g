import openai
import csv
import pandas as pd
import os

openai.api_key = "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"

def query_for(x):
    schema = "Sql table with properties: "
    df = pd.read_csv(x, header=0)
    for i in df.columns:
        schema = schema + "," + i

    messages = []
    print(schema)
    while input!="quit()":
        messages.append({"role":"user","content":schema})
        message = input("You: ")
        if str(message).lower()=="change" and len(message)<25:
            n = input("Enter another table name: ")
            query_for(find_file(n))
        else:
            messages.append({"role":"user","content":message})
            response = openai.ChatCompletion.create(model= "gpt-3.5-turbo",messages = messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role":"assistant" , "content":"reply"})
            print("\n"+reply+"\n")

def find_file(x):
    files = []
    for i in os.listdir("csvs"):
        files.append(str(i))
    for i in files:
        c = i.lower()
        d = x.lower()
        if d in c:
            file = i
            return file


first = input("Enter a table name: ")

query_for(find_file(first))




#   A query for names where billing city is surat, bipoc head is Modi and active program cohort is 0.
#   A query for id where anual budget greater than lakh , orgaization type is sevice an sponsor is jio.