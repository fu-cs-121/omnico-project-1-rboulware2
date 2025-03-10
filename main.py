# =============================================================================
# OmniCo Confidential
# -------------------
# This source code contains proprietary information of OmniCo.
# =============================================================================

def main():
    # Initialize the stats dictionary for each algorithm
    stats = {
        'JoyStream': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0,
            'avg_happiness': 0,
            'avg_duration': 0
        },
        'SerenityFlow': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0,
            'avg_happiness': 0,
            'avg_duration': 0
        },
        'DeepPulse': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0,
            'avg_happiness': 0,
            'avg_duration': 0
        }
    }
    # Open the CSV file and read data
    with open('euphoria_data.csv', 'r') as file:
        # Skip the header line
        header = file.readline()

        # Read each line in the file
        for line in file:
            # Remove any trailing whitespace characters like newline
            line = line.strip()

            # Split the line into a list of values
            columns = line.split(',')

            # Assign each column to a variable
            user_id = columns[0]
            algorithm = columns[1]
            
            session_duration = int(columns[2])
            happiness_rating = int(columns[3])
            # TODO: DONE Define session_duration and happiness_rating variables and convert them to integers
            # Hint: Use the int() function to convert strings to integers
            # session_duration = ?
            # happiness_rating = ?

            # Update stats based on the algorithm
            if algorithm in stats:
                stats[algorithm]['total_happiness'] += happiness_rating
                stats[algorithm]['total_duration'] += session_duration
                stats[algorithm]['session_count'] += 1
            else:
                # Handle any unexpected algorithm names
                print(f"Unknown algorithm: {algorithm}")

    # TODO: DONE Calculate averages for each algorithm
    for algorithm in stats:
        stats[algorithm]['avg_happiness'] = stats[algorithm]['total_happiness'] / stats[algorithm]['session_count']
        stats[algorithm]['avg_duration'] = stats[algorithm]['total_duration'] / stats[algorithm]['session_count']  

    # For each algorithm in the stats dictionary:
    #   - Calculate avg_happiness = total_happiness / session_count
    #   - Calculate avg_duration = total_duration / session_count
    #   - Store these back into the stats dictionary under 'avg_happiness' and 'avg_duration'
    
    # TODO: Determine the algorithm with the highest average happiness rating
    # Initialize variables to keep track of the highest average happiness and the corresponding algorithm
    # Loop through stats to compare avg_happiness values
    highest_avg_happiness = 0
    happiest_algorithm = ""
    
    for algorithm, happiness in stats.items():
        if happiness['avg_happiness'] > highest_avg_happiness:
            highest_avg_happiness = happiness['avg_happiness']
            happiest_algorithm = algorithm
    # print(f"{highest_avg_happiness}, {happiest_algorithm}")

    # TODO: Determine the algorithm with the longest average session duration
    # Initialize variables to keep track of the longest average duration and the corresponding algorithm
    # Loop through stats to compare avg_duration values

    longest_duration = 0
    longest_algorithm = ""
    for algorithm, duration in stats.items():
        if duration['avg_duration'] > longest_duration:
            longest_duration = duration['avg_duration']
            longest_algorithm = algorithm
    # print(f"{longest_duration}, {longest_algorithm}")
   
    # TODO: Print the report
    # Use print statements to display the results in a formatted way
    # Follow the structure provided in the example output
    print("Euphoria User Engagement Analysis Report\n", "-" * 40)
    print("\n Average Happiness Rating per Algorithm:")
    for algorithm, happiness in stats.items():
        print(f"-{algorithm}: {happiness['avg_happiness']}")
    print("\n Total Number of Sessions per Algorithm:")
    for algorithm, session in stats.items():
        print(f"-{algorithm}: {session['session_count']}")
    print("\n Average Session Duration per Algorithm:")
    for algorithm, duration in stats.items():
        print(f"-{algorithm}: {duration['avg_duration']}")
    print("\n Highest Average Happiness Rating: ")
    print(f"- {happiest_algorithm} with an average happiness rating of {highest_avg_happiness}.")
    print("\n Longest Average Session Duration: ")
    print(f"- {longest_algorithm} with an average session duration of {longest_duration} minutes")

if __name__ == "__main__":
    main()
    