# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path
file_to_load=os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Resources","election_analysis.txt")

#initialize a vote counter
total_votes=0

#Candidate options and candidate votes
candidate_options = []
candidate_votes={}

#Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #Read the header row
    headers=next(file_reader)

    # Print each row in the CSV file 
    for row in file_reader:
        
        #2. Add to the total vote count.
        total_votes+=1
        #Print the candidate name from each row
        candidate_name=row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
with open(file_to_save, "w") as txt_file : 
    # Print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Track the winning candidate, vote count, and percentage.
    winning_candidate =""
    winning_count=0
    winning_percentage=0

    # Determine the percentage of votes for each candidate by looping through the counts.
    #1. Iterarte throught the candidate list
    for candidate_name in candidate_votes:

    # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    #1. Determine if the votes are greater than the winning count
        if (votes>winning_count) and (vote_percentage > winning_percentage):
    #2. If true then set winning_count = votes and winning percent = vote percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
   
# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
    # Save the results to our text file.

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the final vote count to the text file.
    txt_file.write(winning_candidate_summary)

