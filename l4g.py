import os
import csv
from csv import *
import time
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch
from datetime import datetime



folder = "csvf/"
files = []
updated_files=[]

import_model = "cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual"
tokenizer  = AutoTokenizer.from_pretrained(import_model)
model =AutoModelForSequenceClassification.from_pretrained(import_model)

def find_score(x):

    token = tokenizer.encode(x,return_tensors ="pt")
    result = model(token)
    score = int(torch.argmax(result.logits)) + 1
    
    return int(score)


def update_score(x,y):

    good_score=["good_at_score"]
    good=[]

    do_score = ["do_better_score"]
    do=[]
    ignore = ["",'',"Nan","N/A",'N/a','n/a',"NA",".",",","?"]


    with open(x,"r") as file:
        read = csv.reader(file)
        for i in read:
            good_at = i[12]
            do_better = i[13]
            good.append(good_at)
            do.append(do_better)
    for i in good[1:]:
                score = find_score(i)
                good_score.append(str(score))
                
    for j in do[1:]:
                score2 = find_score(j) 
                do_score.append(str(score2))
        
    with open(x, 'r') as read_obj, \
                    open(y, 'w', newline='') as write_obj:
                csv_reader = reader(read_obj)
                csv_writer = writer(write_obj)
                count = 0
                for row in csv_reader:
                    row.append(good_score[count])
                    row.append(do_score[count])
                    csv_writer.writerow(row)
                    count = count + 1 



def duplicate_csv(x):
        with open(os.path.join(folder, "x"+x),"x") as file:
                with open(x, 'w', newline='') as write_obj:
                        csv_reader = reader(file)
                        csv_writer = writer(write_obj)




for filename in os.listdir(folder):
        
        
        if filename.startswith("x") == False:
            if filename not in files:    
                    duplicate_csv(filename)
                    if filename not in files:
                        files.append(filename)    

                    time.sleep(5)


for i in files:            
            k = folder+str(i)
            j = folder+"x" +str(i)
            print(k,j)
            update_score(k,j)
            updated_files.append(j)   


print("Files duplicated are:",files)                    
print("Updated files are:",updated_files)
