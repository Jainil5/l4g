import csv

def input_analyze(x):
    good_input=[]
    do_input=[]
    good_score=[]
    do_better_score=[]
    good=[]
    do=[]
    pos=0
    neu=0
    neg=0
    pos2=0
    neu2=0
    neg2=0
    ignore = ["",'',"Nan","N/A",'N/a','n/a',"NA",".",",","?"]

    with open(x,"r") as file:
        read = csv.reader(file)
        for i in read:
            good_input.append(i[12])
            do_input.append(i[13])
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

    #Food   
    food=[]
    foodL=["food","taste","tasty","eat"] 
    for i in range(len(good_input)):
        for j in foodL:
            if j in str(good_input[i]).lower():
                food.append(good_score[i])
    for i in range(len(do_input)):
        for j in foodL:
            if j in str(do_input[i]).lower():
                food.append(do_better_score[i])
    food_pos = 0
    food_neg = 0
    for i in food:
        x=int(i)
        if x==2 or x==3:
            food_pos+=1
        elif x==1:
            food_neg+=1

    #Support and help
    support=[]
    supportL=["support","help"]
    for i in range(len(good_input)):
        for j in supportL:
            if j in str(good_input[i]).lower():
                support.append(good_score[i])
    for i in range(len(do_input)):
        for j in supportL:
            if j in str(do_input[i]).lower():
                support.append(do_better_score[i])
    sup_pos = 0
    sup_neg = 0
    for i in support:
        x=int(i)
        if x==2 or x==3:
            sup_pos+=1
        elif x==1:
            sup_neg+=1        

    #Security
    security = []
    securityL=["secure","security","safe","safety"]
    for i in range(len(good_input)):
        for j in securityL:
            if j in str(good_input[i]).lower():
                security.append(good_score[i])
    for i in range(len(do_input)):
        for j in securityL:
            if j in str(do_input[i]).lower():
                security.append(do_better_score[i])
    sec_pos = 0
    sec_neg = 0
    for i in security:
        x=int(i)
        if x==2 or x==3:
            sec_pos+=1
        elif x==1:
            sec_neg+=1 

    #Service
    service=["service","friendly"]        
    
    print("Got",pos,"positive,",neu,"neutral,",neg,"negative out of",len(good),"in good at field.")
    print("Got",pos2,"positive,",neu2,"neutral,",neg2,"negative out of",len(do),"in do_better at field.")
    if len(food)!=0:
        print("Food:",food_pos,food_neg)
    if len(support)!=0:
        print("Support and help:",sup_pos,sup_neg)
    if len(security)!=0:
        print("Security:",sec_pos,sec_neg)    


input_analyze("ag1.csv")            