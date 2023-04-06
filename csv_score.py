import senti as sa
import csv
from csv import *


def read_csv(x):

    good_score=["good_at_score"]

    do_score = ["do_better_score"]

    ignore = ["",'nan',"Nan","N/A",'N/a','n/a',"NA",".",",","?"]


    with open(x,"r") as file:
        read = csv.reader(file)
        for i in read:
            good_at = i[12]
            if good_at in ignore :
                score = 2
            else:
                score = sa.score(good_at)
            good_score.append(str(score))

            #do better
            do_better=i[13]
            if do_better in ignore:
                score2 = 2
            else:
                score2 = sa.score(do_better) 
            do_score.append(str(score2))
    
    with open(x, 'r') as read_obj, \
                    open('score.csv', 'w', newline='') as write_obj:
            csv_reader = reader(read_obj)
            csv_writer = writer(write_obj)
            count = 0
            for row in csv_reader:
                row.append(good_score[count])
                row.append(do_score[count])
                csv_writer.writerow(row)
                count = count + 1 

                