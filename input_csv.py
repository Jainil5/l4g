import os
import csv

meet_needs_input=[]
meet_needs_count={}

respect_input=[]
respect_count={}
files=[]
qualities=[]
changes = []
ignore = ["",'nan',"Nan","N/A",'N/a','n/a',"NA","Nothing",".",",","?"]


for filename in os.listdir('csvf/'):
    with open(os.path.join('csvf/', filename), 'r') as f:
        if filename not in files:
            files.append(filename)
        read = csv.reader(f)
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


print(meet_needs_count)
print(respect_count)
print("Files read are: ",files)
print("Accepted files: ",meet_needs_input)