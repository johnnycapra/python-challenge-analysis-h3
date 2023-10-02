import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

election_results = {}
 
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    total_votes = 0
    for row in csvreader:
        total_votes += 1 
        if row[2] not in election_results:
            election_results[row[2]]= 0
        election_results[row[2]] += 1
    
    top_results = 0
    candidate_list = ""
    for candidate, votes_count in election_results.items():
        if votes_count > top_results:
            top_results = votes_count
            election_winner = candidate
        vote_percent = round((votes_count/total_votes)*100,3)
        list_convert = str(f'{candidate}: {vote_percent}% ({votes_count})\n')
        candidate_list += list_convert

text_output = ('Election Results\n'
               '------------------------\n'
               f'Total Votes: {total_votes}\n'
               '------------------------\n'
               f'{candidate_list}'
               '------------------------\n'
               f'Winner: {election_winner}\n'
               '------------------------\n'

)

print(text_output)

election_analysis = os.path.join("analysis", "election_analysis.txt")
with open(election_analysis, "w") as file:
    file.write(text_output)
file.close()

