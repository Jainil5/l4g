import sentiment_analysis as sa
import csv
from csv import *

good_score=["good_at_score"]

do_score = ["do_better_score"]

ignore = ["",'nan',"Nan","N/A",'N/a','n/a',"NA",".",",","?"]
good=[]
do=[]

x = "ag.csv"
y = "ag2.csv"


def update(x,y):
    with open(x,"r") as file:
        read = csv.reader(file)
        for i in read:
            good_at = i[12]
            do_better = i[13]
            good.append(good_at)
            do.append(do_better)
    for i in good[1:]:
                score = sa.score(i)
                good_score.append(str(score))
                
    for j in do[1:]:
                score2 = sa.score(j) 
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


update(x,y)
                