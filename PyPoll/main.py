# Module 3 Challenge (PyPoll)

# Instructions / delivery:
#       1. The total number of votes cast
#       2. A complete list of candidates who received votes
#       3. The percentage of votes each candidate won
#       4. The total number of votes each candidate won
#       5. The winner of the election based on popular vote

#Import Modules
import os, csv

# Set the path for the input file
csvpath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "Financial_Analysis.txt")

# Create the list and variables that we are going to use
total_votes = 0
winner_votes = 0
winner = None
candidates = []
votes_by_candidate = {}

# Read the input file and calculate data
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    csv_header = next(csvreader)
        
    for row in csvreader:
        # 1. Count the total number of votes
        total_votes += 1
        # Add the candidate to the list of candidates (if not already there)
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
        # Count the number of votes for each candidate
        if candidate not in votes_by_candidate:
            votes_by_candidate[candidate] = 0
        votes_by_candidate[candidate] += 1
        # Check if this candidate has more votes than the current winner
        if votes_by_candidate[candidate] > winner_votes:
            winner = candidate
            winner_votes = votes_by_candidate[candidate]

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    votes = votes_by_candidate[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# write the results on a text file
with open(output_path, 'w') as text:
    text.write("Election Results (PyPoll)\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-------------------------\n")
    for candidate in candidates:
        votes = votes_by_candidate[candidate]
        percentage = (votes / total_votes) * 100
        text.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    text.write("-------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("-------------------------")
