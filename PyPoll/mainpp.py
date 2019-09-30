import os
import csv
from collections import Counter
csvpath = 'election_data.csv'

def poll_results(csv_reader):
    # dictionary for storing results
    results = {}
    # define variables for storing each iteration
    total_votes = 0
    candidates = []
    votes_pc = []
    vote_percent = []

    # loop for grabbing data
    for row in (csv_reader):
        total_votes += 1
        cur_cand = (str(row[2]))
        if cur_cand not in candidates:
            candidates.append(cur_cand) 
        if row[2] in results.keys():
            results[row[2]] = results[row[2]] + 1
        else:
            results[row[2]] = 1
   

     # store in dictionary
    for key, value in results.items():
        candidates.append(key)
        votes_pc.append(value)

    # creates vote percent list
    for pc in votes_pc:
        vote_percent.append(round(pc/total_votes*100, 1))

    poll_results = list(zip(candidates, vote_percent, votes_pc))
    
    #find the winner of the election
    top_vote = 0
    winner = "none"
    for each in poll_results:
        if votes_pc > top_vote:
            winner = candidates
            top_vote = votes_pc

    # Print Results
    print(f"Election Results")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
    for each in poll_results:
        print(each)
    print("------------------------")
    print(f'Winner: {winner}!')
    

with open(csvpath, newline='') as csvfile:
    poll_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(poll_reader)
    poll_results(poll_reader)

    



