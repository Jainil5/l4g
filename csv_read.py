import csv

meet_needs_input=[]
meet_needs_count={}

respect_input=[]
respect_count={}

qualities=[]

changes = []

ignore = ["",'nan',"Nan","N/A",'N/a','n/a',"NA","Nothing",".",",","?"]
with open("ag.csv","r") as file:
    read = csv.reader(file)
    for i in read:
        
        
        #Meet needs
        meet = i[8]
        if meet not in ignore:
            meet_needs_input.append(meet)

        for j in meet_needs_input:
            meet_needs_count.update({j:meet_needs_input.count(j)})


        #respect
        respect = i[9]
        if respect not in ignore:
            respect_input.append(respect)

        for j in respect_input:
            respect_count.update({j:respect_input.count(j)})

        #good at
        good_at = i[12]
        if good_at not in ignore:
            qualities.append(good_at)
        
        #do better
        do_better=i[13]
        if do_better not in ignore:
            changes.append(do_better)

    print(changes)
        

'''
0.DATE_CREATED
1.MEMBER_ID
2.SURVEY_ID
3.IP_ADDRESS
4.REC_ID
5.SL1
6.SL2
7.net_promoter_score_listen_for_good
8.l4g_meet_needs
9.l4g_respect
10.l4g_easy_get_services
11.l4g_connected
12.l4g_good_at
13.l4g_do_better
14.l4g_age
15.l4g_gender
16.l4g_race
'''
    