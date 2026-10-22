IPL Batting Performance Analysis (2007–2024)

Project Overview:
This project analyzes Indian Premier League (IPL) batting statistics from 2007 to 2024 using Python and Power BI. It focuses on evaluating player performance, batting volume, scoring efficiency, and venue-level strike-rate differences through data cleaning, DAX measures, and interactive visualizations.

Objectives:
Analyze overall batting performance using key performance indicators.
Compare players based on runs scored and balls faced.
Explore the relationship between batting volume and run production.
Compare batting strike rates across venues.
Build an interactive dashboard to summarize historical IPL batting statistics.

Tech Stack:
Power BI – Dashboard development and data visualization
DAX – Measures and analytical calculations
Python – Data inspection and preprocessing
Pandas – Data cleaning and transformation
NumPy – Numerical data operations

Data Preparation:
The dataset was processed using Python and Pandas to prepare it for analysis.

Inspected dataset structure and assessed missing values.
Removed unnecessary commentary, text, and reference columns.
Identified and removed duplicate records.
Converted Boolean fields to appropriate data types.
Exported the cleaned dataset to CSV for Power BI integration.

Dashboard Features:
1. Batting Performance KPIs
Summarizes overall batting statistics through KPI cards displaying total runs, average strike rate, distinct match count, and total sixes.

2. Player Batting Volume
Uses a horizontal bar chart to compare players by total balls faced and identify batters with the highest batting volume.

3. Runs vs. Balls Faced
Uses a bubble chart to explore the relationship between balls faced and total runs, helping compare player contribution and scoring output.

4. Venue-Level Strike-Rate Analysis
Compares average batting strike rates across venues to explore differences in scoring efficiency.

Key Metrics:
Total Runs: Aggregate batter runs across the selected records.
Average Strike Rate: Batting scoring rate, calculated using runs and balls faced according to the chosen aggregation method.
Total Balls Faced: Aggregate balls faced by batters.
Total Sixes: Total sixes recorded in the batting data.
Distinct Matches: Count of unique match identifiers.

Analytical Approach:
Python was used for data inspection and preprocessing, while Power BI and DAX were used to aggregate batting statistics and create comparative visualizations.

The analysis focuses on three dimensions:

Batting volume: Balls faced and total runs.
Scoring efficiency: Strike-rate comparisons.
Venue performance: Differences in batting strike rates across grounds.

Key Questions Explored:
Which batters faced the most balls?
How does batting volume relate to total run production?
How do batting strike rates differ across venues?
How can historical IPL batting statistics be summarized using interactive KPIs and visualizations?

Project Outcome:
Developed a Power BI dashboard that consolidates historical IPL batting statistics into an interactive analytical view. The project demonstrates practical skills in data preprocessing, DAX-based calculations, KPI development, comparative analysis, and sports data visualization.

Data Limitations:
The accuracy of the analysis depends on the source dataset's structure and granularity. Duplicate records and repeated or cumulative statistics must be handled carefully to prevent double-counting. Match counts should use distinct match identifiers, and strike rates should be calculated using appropriate batter runs and balls faced. Venue and player comparisons should also be interpreted in the context of sample sizes and seasonal differences.

Skills Demonstrated:
Python · Pandas · NumPy · Power BI · DAX · Data Cleaning · Data Analysis · Data Visualization · Dashboard Development · Sports Analytics