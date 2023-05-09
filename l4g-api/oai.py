import openai

openai.api_key = "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"
ask="How arre you"
completion = openai.ChatCompletion.create( model= "gpt-3.5-turbo",messages = [{"role":"user","content":ask}])
print(completion["choices"][0]["message"]["content"])