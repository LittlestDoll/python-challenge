import os
import csv 
csvpath = os.path.join("election_data_2.csv")

total_votes = 0
candidates = {}

with open(csvpath, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    for row in csvreader:
        total_votes += 1
        if row['Candidate'] in candidates:
            candidates[row['Candidate']] += 1
        else:
            candidates[row['Candidate']] = 1

     
print("Election Results")
print("--------------------")  
print("Total Votes: " + str(total_votes)) 
print("--------------------")

for can_name in candidates:
    votes = candidates[can_name]
    print("{}: {:.2%} ({})".format(can_name, votes / total_votes, votes))

print("--------------------")  
winner = sorted(candidates, key=candidates.get, reverse=True)[0]
print("Winner: " + winner)
print("--------------------")  
    