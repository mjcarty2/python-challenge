<<<<<<< HEAD
import csv
import os

file = "election_data.csv"

total_votes = 0
candidate = []
votes_count = []

with open(file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
   
    for row in reader:
        total_votes = total_votes+1
        if row[1] in candidate:
            vote = candidate.index(row[2])
            votes_count[vote]+=1
        else:
            candidate.append(str(row[2]))
            votes_count.append(1)

print("Election Results")
print("Total Votes: "+str(total_votes))
for x in range(0, len(candidate)):
        print(candidate[x]+": "+str(round((100*votes_count[x]/total_votes),2))+"% "+str(votes_count[x]))
winner = votes_count.index(max(votes_count))
print("Winner: "+candidate[winner])


election_results_file = open("Results.txt", "w")
election_results_file.write("Elections Results\n")
election_results_file.write(f'Total Votes: {total_votes}\n')
for x in range(0, len(candidate)):
        election_results_file.writerow([candidate[x], str(round((100*votes_count[x]/total_votes),2)), str(votes_count[x])])
election_results_file.write(f'Winner: {winner}')
=======

>>>>>>> 83f9b72a436c2c2a6af1cd26935dd484e5c5a472
