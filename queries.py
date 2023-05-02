import openai
import csv
import pandas as pd

openai.api_key = "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"
schema = "SFAccounts with properties: "

df = pd.read_csv("SFAccounts.csv",header = 0)
for i in df.columns:
    schema = schema + ","+i

messages = []
print(" Write queries for "+schema)
while input!="quit()":
    messages.append({"role":"user","content":schema})
    message = input("You: ")
    messages.append({"role":"user","content":message})
    response = openai.ChatCompletion.create(model= "gpt-3.5-turbo",messages = messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant" , "content":"reply"})
    print("\n"+reply+"\n")

#A query for names where billing city is surat, bipoc head is Modi and active program cohort is 0.