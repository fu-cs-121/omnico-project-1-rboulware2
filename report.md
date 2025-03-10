# Euphoria User Engagement Analysis Report

**Author:** [Royton Boulware]  
**Date:** [3-10-25]

---

## Introduction

[Provide a brief overview of the project objectives and the importance of the analysis.]
[This project compares user engagement data from three different social VR programs: JoyStream, SerenityFlow, and DeepPulse. The objective of this report is to contrast feedback from the three programs and determine some statistics for company use.]

## Methodology

[Describe the steps you took to perform the analysis, including any calculations and reasoning behind them.]
[To perform my analysis, multiple steps had to be performed. To make the data easier to read and handle, it was read in from a CSV file to a python dictionary. This allowed me to add columns from my calculations and perform looped calculations on the data. To begin the calculation portion of this project, I looped through each of the rows in the CSV file, storing happiness, session duration, and total sessions into the vairables total_happiness, total_duration, and session_count. I used these varaibles for calculating average happiness and average session duration by dividing total_happiness by session_count and total_duration by session count. Next, I calculated which variable had the highest happiness rating by defining the highest_avg_happiness and happiest_algorithm variables, which I set at zero, then looping through the data and storing the highest happiness rating into highest_avg_happiness and the corresponding algorithm into happiest_algorithm. I repeated this process to calculate the longest average session duration but with the variables longest_duration and longest_algorithm. ]

## Results

- **Average Happiness Rating per Algorithm**

  - JoyStream: 8.50
  - SerenityFlow: 7.00
  - DeepPulse: 5.00

- **Total Number of Sessions per Algorithm**

  - JoyStream: 4
  - SerenityFlow: 3
  - DeepPulse: 3

- **Average Session Duration per Algorithm**

  - JoyStream: 37.50 minutes
  - SerenityFlow: 30.00 minutes
  - DeepPulse: 45.00 minutes

- **Highest and Lowest Performers**
  - Highest Average Happiness Rating: 8.50
  - Longest Average Session Duration: 45.00

## Observations and Insights

[Discuss any patterns, anomalies, or noteworthy findings from your analysis. Include any ethical considerations or unexpected results, especially related to the DeepPulse algorithm.]
[It is important to take note of the purpose of the algorithms before discussing findings. JoyStream focuses on positivity, SerenetyFlow on calming, and DeepPulse on vaired emotional content. These descriptions help to verify some of my findings. JoyStream had the highest average happiness rating, which would make sense as it specializes in positivity. A pattern that became apparent as I was analyzing my findings was that SerenityFlow was a low performer in many of the categories. DeepPulse consistently had a higher session duration, which is something I would want to look into further. Ethically, these programs should be marketed and consumed with caution, as emotions can be difficult to manipulate and these programs may present some users with unpleasent experiences. This applies especially to DeepPulse, as it is not well defined in it's purpose, which may not bode well for emotionally unstable users. ]

## Conclusions and Recommendations

[Summarize your conclusions based on the results. Provide any recommendations for next steps or further analysis.]
[In conclusion, I believe that the program that brings the most straightforward benefits to our company is the JoyStream algorithm. Also, it is my reccommendation to cut the SerenityFlow and DeepPulse algorithms. SerenityFLow does not seem to be benefitting the company in anyway based on customer engagement, and there are some ethical issues with DeepPulse that may want to be discussed by human resources and management before proceeding with the program. However, based upon the users longer engagement with the DeepPulse, I would encourage some more research and development to combine aspects of it with the JoyStream algorithm for maximum user experience.  ]

---

_This report contains confidential information proprietary to OmniCo. Unauthorized use or disclosure is strictly prohibited._
