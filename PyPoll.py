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
print("The time right now is ", now)

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
    print(headers)





