import os
import openai
import re


openai.api_key = "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"




num=[]
def Query(x):
    if len(x)>1:
        y = str(x).lower()
        z = re.findall(".* volume to. *",y)
        w = y.index("to")
        if "set volume" in y:
            v=""
            for i in y:
                if i.isnumeric():
                    v+=i
            if v.isnumeric():
                vol=int(v)
            return y
        elif "change brightness" in  y:
            return y
        else:
            default = "SQL table, with their properties: L4G(id,bill_address,billing_address_city,mrp,items)."
            ask = default + str(x)
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ask}])
            return str("\nQuery: " + x + "\n\n" + completion["choices"][0]["message"]["content"] + "\n")

    else:
        return "Sorry, I do not understand this can you please elaborate."
    
 
print(Query("set volume to 100"))

