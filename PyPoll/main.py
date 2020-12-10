import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")
# Read in the CSV file
with open(election_csv, "r") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header
    next(csvreader, None)

    # Declare the variables
    total_votes_cast = []
    candidate_list = []
    candidates_unique =[]
    votes = {}
    percentage = []
    
    for row in csvreader:
        # Total number of votes is length of first column - each voter ID is unique, print length in analysis
        total_votes_cast.append(row[0])

        # Assign third column to a list with each time a candidate was voted
        candidate_list.append(row[2])

        # Assign a list of candidates, unique values from candidate_list
        if row[2] not in candidate_list:
            candidates_unique.append(row[2])

    # Count the number of votes for each candidate
    for item in candidate_list:
        if item in votes:
            votes[item] += 1
        else:
            votes[item] = 1

    # Calculate the percentage compared to total votes
    for i in votes:
        percentage.append(votes[i]/len(total_votes_cast)*100)
        

# The 'winner' is the one with the maximum value of votes for each candidate
winner = max(votes, key=votes.get)

# Zip lists together where;
# key=names
# values=votes for each candidate
cleaned_csv = zip(votes.keys(), votes.values(), percentage)
clean_list = list(cleaned_csv)



print("Election Results")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(f"Total Votes: {len(total_votes_cast)}")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
for j in clean_list:
   print(str(j[0]) + ": " + str(j[2]) + " (" + str(j[1]) + ")")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(f"Winner: {winner}")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    

# Export the above results as a text file in analysis folder
# Method from PyBank didn't work with for loop
write_file = f"Analysis/election_results.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
filewriter.write(f"Total Votes: {len(total_votes_cast)}\n")
filewriter.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
for j in clean_list:
  filewriter.write(str(j[0]) + ": " + str(j[2]) + " (" + str(j[1]) + ")")
filewriter.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

#close file
<<<<<<< HEAD
filewriter.close()
=======
filewriter.close()
>>>>>>> 653e01f9e241cb4f3389289b9019973fee35f516
