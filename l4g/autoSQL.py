import os
import openai

openai.api_key = "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"

def Query(x):
    default = "SQL table, with their properties: L4G(id,bill_address,billing_address_city,mrp,items)."
    ask = default + str(x)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ask}])
    print(str("\nQuery: " + x + "\n\n" + completion["choices"][0]["message"]["content"] + "\n"))


Query("A query to list the items with billing address city surat and mrp greater than 1000.")
