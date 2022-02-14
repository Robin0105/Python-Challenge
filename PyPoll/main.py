# Import os and csv modules
import os
import csv

# Set the path for the CSV file

PyPollcsv = os.path.join("Resources","election_data.csv")

# Create the lists to store data and initialize total_votes

total_votes = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path

with open(PyPollcsv, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)
    # Conduct the ask
    for row in csv_reader:
        # Count total number of votes
        total_votes = total_votes + 1
        # Set candidate names to candidatelist
        candidatelist.append(row[2])
        # Create set from the candidatelist for unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y - total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z - percent of total votes per candidate
        z = round((y/total_votes)*100, 5)
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_votes))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


with open('analysis/election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")

