# PyPoll Challenge

import pandas as pd 

#Specifying path to CSV file
file_path = 'C:\\Users\\lnata\\GitHub\\python-challenge\\PyPoll\\Resources\\election_data.csv'

# Read CSV file
df = pd.read_csv(file_path)

# Space between code and output on Terminal to make my output organized
print(" ")

# Headers
print("Election Results")

# Spacers
print("-------------------------")

# Calculate total votes by counting rows
total_votes = len(df)

# Print Total Votes
print("Total Votes: " + str(total_votes))

# Spacers
print("-------------------------")

# Calculate the total number of votes each candidate received
c1 = "Charles Casper Stockham"
c2 = "Diana DeGette"
c3 = "Raymon Anthony Doane"

# Calculate total number of votes each candidate won
c1_won = df[df['Candidate'] == c1].shape[0]
c2_won = df[df['Candidate'] == c2].shape[0]
c3_won = df[df['Candidate'] == c3].shape[0]
votes_won = df['Candidate'].value_counts()

# Calculate the percentage of votes each candidate won
percent_c1_won = (c1_won / total_votes) * 100
percent_c2_won = (c2_won / total_votes) * 100
percent_c3_won = (c3_won / total_votes) * 100

# Who won?
winner = votes_won.idxmax()

# Print the results
print("Charles Casper Stockham: " + format(percent_c1_won, '.3f') + "%" + " (" + str(c1_won) + ")")
print("Diana DeGette: " + format(percent_c2_won, '.3f') + "%" + " (" + str(c2_won) + ")")
print("Raymon Anthony Doane: " + format(percent_c3_won, '.3f') + "%" + " (" + str(c3_won) + ")")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

# Export!
output_file_path = 'PyPoll_analysis_summary.txt'
with open(output_file_path, 'w') as file:
    file.write("Election Results" + '\n')
    file.write("-------------------------" + '\n')
    file.write("Total Votes: " + str(total_votes) + '\n')
    file.write("-------------------------" + '\n')
    file.write("Charles Casper Stockham: " + format(percent_c1_won, '.3f') + "%" + " (" + str(c1_won) + ")" + '\n')
    file.write("Diana DeGette: " + format(percent_c2_won, '.3f') + "%" + " (" + str(c2_won) + ")" + '\n')
    file.write("Raymon Anthony Doane: " + format(percent_c3_won, '.3f') + "%" + " (" + str(c3_won) + ")" + '\n')
    file.write("-------------------------" + '\n')
    file.write("Winner: " + str(winner) + '\n')
    file.write("-------------------------" + '\n')
