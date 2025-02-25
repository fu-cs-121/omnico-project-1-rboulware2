# Data Analysis Simulation Assignment

{{user.first_name }}, it's your first day at OmniCo and you open your email to see the following message:

<div style="display: flex; flex-direction: column; border: 1px solid #ddd; font-size: 16px; font-family: sans-serif; line-height: 1.2em; box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;">
<div style="border-bottom: 1px solid #ddd; width: 100%; padding: 10px 20px; color: #666;">From: Sophia Lewis (sophia.lewis@omni.co)</div>
<div style="border-bottom: 1px solid #ddd; width: 100%; padding: 10px 20px; color: #666;">Subject: Analyzing Euphoria's User Engagement Data</div>
<div style="padding:20px 40px;">
Dear {{user.first_name}},

Welcome to your first day at OmniCo! I hope you're settling in well.

I have an important task for you regarding our social VR platform, **Euphoria**. We've recently implemented three different content feed algorithms to see how they affect user engagement and mood:

- **JoyStream**: Focuses on positive and uplifting content
- **SerenityFlow**: Delivers calming and peaceful experiences
- **DeepPulse**: Presents a wider range of emotional content

We've collected data from user sessions with each algorithm, and I'd like you to analyze this information to help us understand which algorithm is performing best.

I've added a data file called `euphoria_data.csv` to your repository. It contains information about each user session, including which algorithm was used, how long the session lasted, and the user's happiness rating after the session.

Please analyze this data and prepare a report with your findings. We're particularly interested in which algorithm produces the highest happiness ratings and which one keeps users engaged for the longest time.

Looking forward to your insights!

Best regards,

Sophia Lewis
Lead Research Analyst
OmniVerse Division, OmniCo

<div style="font-size: 11px; color: #666">
CONFIDENTIALITY NOTICE: This message contains proprietary information of OmniCo and is protected by the OmniCo Cybernetic Legal AI (CLAIR) system. Unauthorized use or disclosure is strictly prohibited.
</div>

</div>
</div>

---

# Project Instructions

In this assignment, you'll work with a real-world scenario where you need to analyze data to help make business decisions. You'll practice new skills including:

- Reading data from CSV files
- Processing and analyzing the data
- Calculating statistics
- Presenting findings in a professional format

## Learning Objectives

- Understand how to read and parse data from files
- Apply programming concepts to solve real data problems
- Calculate and interpret basic statistics
- Present findings effectively

## Getting Started

1. **Set Up Your Project**

   - Clone the repository from the [classroom link](https://classroom.github.com/a/2DJMmKAd)
   - Open a new window in VSCode (File > New Window)
   - Click the Source Panel (branch icon) and then "Clone Repository"
   - Paste in the URL and select a location to save the repository
   - Open the repository folder in VSCode
   - Add your name to the top part of your `report.md` and commit/push it back to Github

2. **Understanding the Data**
   - The file `euphoria_data.csv` contains the following columns:
     - `user_id`: A unique identifier for each user
     - `algorithm`: Which content algorithm was used (JoyStream, SerenityFlow, or DeepPulse)
     - `session_duration`: How long the user session lasted, in minutes
     - `happiness_rating`: The user's self-reported happiness rating after the session (1-10 scale)

## Step-by-Step Tutorial

### Step 1: Understanding File I/O in Python

In Python, we can read data from files using the `open()` function. For CSV files, we typically:

1. Open the file
2. Read each line
3. Process the data in each line
4. Close the file when finished

Here's how we open and read a file:

```python
# Open the file in read mode ('r')
with open('filename.csv', 'r') as file:
    # The 'with' statement automatically closes the file when the block ends

    # Read the header line (column names)
    header = file.readline()

    # Read the rest of the lines
    for line in file:
        # Process each line here
        print(line)  # This will print each line with newline characters

        # To remove whitespace and newline characters:
        clean_line = line.strip()
        print(clean_line)
```

### Step 2: Parsing CSV Data

CSV (Comma-Separated Values) files store data as text with values separated by commas. To parse each line:

```python
# Split the line into values using comma as separator
columns = line.split(',')

# Now 'columns' is a list containing each value from the line
# For example, if line is "101,JoyStream,45,8", then:
# columns[0] would be "101" (user_id)
# columns[1] would be "JoyStream" (algorithm)
# columns[2] would be "45" (session_duration)
# columns[3] would be "8" (happiness_rating)
```

### Step 3: Converting String Values to Numbers

Values read from a file are always strings, even if they represent numbers. To perform calculations, we need to convert them to numeric types:

```python
# Convert string to integer
session_duration = int(columns[2])

# Convert string to float (for decimal numbers)
happiness_rating = int(columns[3])
```

### Step 4: Organizing Data with Dictionaries

We'll use dictionaries to store and organize our data by algorithm:

```python
# Initialize a dictionary to store statistics for each algorithm
stats = {
    'JoyStream': {
        'total_happiness': 0,
        'total_duration': 0,
        'session_count': 0
    },
    'SerenityFlow': {
        'total_happiness': 0,
        'total_duration': 0,
        'session_count': 0
    },
    'DeepPulse': {
        'total_happiness': 0,
        'total_duration': 0,
        'session_count': 0
    }
}
```

### Step 5: Your Task - Complete the Program

Now, your job is to complete the provided Python program to:

1. Read the CSV data
2. Calculate statistics for each algorithm
3. Determine which algorithm has the highest happiness rating and longest average session duration
4. Print a formatted report of your findings

Open the file `analyze_euphoria.py` and follow the TODO comments to complete the code.

## Requirements

1. **Complete the Python Script**

   - Follow all TODO comments in the code
   - Calculate the following for each algorithm:
     - Average happiness rating
     - Total number of sessions
     - Average session duration
   - Identify which algorithm has the highest average happiness rating
   - Identify which algorithm has the longest average session duration
   - Format and print the results

2. **Write a Report**
   - Complete the `report.md` file with your findings
   - Include your methodology and any insights you discover
   - Make sure your report is professional and well-formatted

## Example Output

Your program should produce output similar to this:

```plaintext
Euphoria User Engagement Analysis Report
----------------------------------------

Average Happiness Rating per Algorithm:
- JoyStream: 8.50
- SerenityFlow: 7.00
- DeepPulse: 5.00

Total Number of Sessions per Algorithm:
- JoyStream: 4
- SerenityFlow: 3
- DeepPulse: 3

Average Session Duration per Algorithm:
- JoyStream: 37.50 minutes
- SerenityFlow: 30.00 minutes
- DeepPulse: 45.00 minutes

Highest Average Happiness Rating:
- JoyStream with an average happiness rating of 8.50

Longest Average Session Duration:
- DeepPulse with an average session duration of 45.00 minutes
```

## Starter Code

Use the starter code in your `main.py` file to complete this assignment.

Make sure you follow the TODO comments and structure your code according to the instructions provided.

## Submission Instructions

When you've completed the assignment:

1. Make sure your code works correctly and produces the expected output
2. Make sure your report is complete and professional
3. Commit and push your changes to your GitHub repository
4. Submit the link to your repository on Canvas

Good luck, and remember that this assignment is designed to help you learn how to apply programming concepts to real-world data analysis tasks!
