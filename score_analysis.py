import csv 
import re
import string 

def input_analyze(x):
    good_score=[]
    do_better_score = []
    good = []
    do = []
    pos=0
    neu=0
    neg=0
    pos2=0
    neu2=0
    neg2=0
    with open("ag.csv","r") as file:
        read = csv.reader(file)
        for i in read:
            good_score.append(i[17])
            do_better_score.append(i[18])
        
        
        for i in good_score:
            if i.isnumeric():
                good.append(int(i))
        for i in do_better_score:
            if i.isnumeric():
                do.append(int(i))
                        
        for x in good:        
            if x == 1:
                neg+=1
                
            if x == 2:
                neu+=1
                    
            if x == 3:
                pos+=1
        
                
        for x in do:        
            if x == 1:
                neg2+=1
                
            if x == 2:
                neu2+=1
                    
            if x == 3:
                pos2+=1

    print("Got",pos,"positive,",neu,"neutral,",neg,"negative out of",len(good),"in good at field.")
    print("Got",pos2,"positive,",neu2,"neutral,",neg2,"negative out of",len(do),"in do_better at field.")

