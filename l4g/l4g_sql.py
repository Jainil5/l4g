import os
import openai

openai.api_key = "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"
ask="Postgres SQL table, with their properties: L4G(id,billing_address,billing_address_city,mrp,items). A query to list the items with billing address city surat and mrp greater than 1000\n"
completion = openai.ChatCompletion.create( model= "gpt-3.5-turbo",messages = [{"role":"user","content":ask}])
print(completion["choices"][0]["message"]["content"])