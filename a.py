import csv
with open("ag.csv","r") as file:
        read = csv.reader(file)
        for i in read:
            good_at = i[12]
            if good_at.startswith("l4g_"):
                continue
            print(good_at)




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
       