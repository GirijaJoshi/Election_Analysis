# In this project, our final Python script will need to be able to deliver the following
# information when the script is run:
#
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

# Import the datetime class from the datetime module.
import datetime as dt
import os
import csv

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)

# # Assign a variable for the file to load and the path.
# # file_to_load = 'Resources/election_results.csv'
# file_to_load = os.path.join("Resources", "election_results.csv")
#
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     # To do: perform analysis.
#     print(election_data)
#
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#
#     # # Write three counties to the file.
#     # txt_file.write("Arapahoe")
#     # txt_file.write("Denver")
#     # txt_file.write("Jefferson")
#     # # output would be
#     # # ArapahoeDenverJefferson
#
#     # # Write three counties to the file.
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")
#     # # outout : Arapahoe, Denver, Jefferson
#
#     # # Write three counties to the file.
#     # txt_file.write("Arapahoe\nDenver\nJefferson")
#     # # output:
#     # # Arapahoe
#     # # Denver
#     # # Jefferson
#
#     # Skills
#     message_to_candidate = (
#         f"Counties in the election. \n"
#         f"------------------------------------------------------------------\n"
#         f"Arapahoe\nDenver\nJefferson")
#     txt_file.write(message_to_candidate)

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    # for row in file_reader:
    #     print(row)
    #     print(row[0])

    # Print the header row.
    headers = next(file_reader)
    # print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate}: received {vote_percentage:.1f}% of the vote.")
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
        # print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

# # 3. Print the total votes.
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)
# print(f"Winning candidate: {winning_candidate}, vote count: {winning_count}, percentage: {winning_percentage:.1f}%.")





