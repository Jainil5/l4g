import os
import openai

openai.api_key = "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"

messages = []
print("Bot: How can I help you?")
while input!="quit()":
    message = input("You: ")
    messages.append({"role":"user","content":message})
    response = openai.ChatCompletion.create(model= "gpt-3.5-turbo",messages = messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant" , "content":"reply"})
    print("\n"+reply+"\n")
