import csv

# Function to analyze election data
def analyze_election_data(file_path):
    # Initialize variables
    total_votes = 0
    candidates = {}
    
    # Read the CSV file
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Skip the header row
        next(csvreader)

        # Loop through each row in the CSV
        for row in csvreader:
            # Extract candidate information
            candidate = row[2]

            # Update total votes
            total_votes += 1

            # Update candidate votes
            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1

    # Determine the winner
    winner = max(candidates, key=candidates.get)

    # Display results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    # Display each candidate's results
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Save results to a text file
    with open("election_results.txt", "w") as text_file:
        text_file.write("Election Results\n")
        text_file.write("-------------------------\n")
        text_file.write(f"Total Votes: {total_votes}\n")
        text_file.write("-------------------------\n")
        
        # Write each candidate's results to the text file
        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        text_file.write("-------------------------\n")
        text_file.write(f"Winner: {winner}\n")
        text_file.write("-------------------------\n")

# Specify the path to the CSV file
file_path = "path/to/election_data.csv"

# Call the function with the file path
analyze_election_data(file_path)