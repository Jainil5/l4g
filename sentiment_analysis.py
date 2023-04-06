from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch

import_model = "Jorgeutd/bert-base-uncased-finetuned-surveyclassification"
tokenizer  = AutoTokenizer.from_pretrained(import_model)
model =AutoModelForSequenceClassification.from_pretrained(import_model)


def score(x):
    token = tokenizer.encode(x,return_tensors ="pt")
    result = model(token)
    score = int(torch.argmax(result.logits)) + 1
    return int(score)




