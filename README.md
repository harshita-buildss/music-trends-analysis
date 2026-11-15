🎧 Music Trends Analysis & Visualization

📌 Project Overview

This project explores music trends using a Spotify tracks dataset. It uses Python and data visualization techniques to analyze music popularity, energy, danceability, song duration, and explicit content.

🎯 Objectives

- Analyze music trends across different genres.
- Identify the most popular music genres.
- Compare energy and danceability of songs.
- Explore music popularity distribution.
- Visualize song duration and explicit content.

📂 Dataset Information

- Total Records: 114,000 (before cleaning)
- Total Features: 20 (before adding the duration column)
- Total Genres: 114
- Data Source: Spotify Tracks Dataset

🛠️ Tools & Technologies

- Python
- Pandas
- Matplotlib
- VS Code

🧹 Data Cleaning

- Checked missing values.
- Removed records with missing song information.
- Removed duplicate records.
- Converted song duration from milliseconds to minutes.

Final cleaned dataset: 113,549 records.

📊 Visualizations

1. Top 10 Most Popular Music Genres
2. Top 10 Highest Energy Genres
3. Music Popularity Distribution
4. Danceability vs Energy
5. Average Song Duration by Genre
6. Explicit vs Non-Explicit Songs

🔍 Key Findings

- Pop-film has the highest average popularity (59.28).
- Death-metal has the highest average energy (0.93).
- Average music popularity is 33.32.
- Average song duration is 3.8 minutes.

▶️ How to Run the Project

1. Install the required libraries:
   
   "python -m pip install pandas matplotlib"

2. Run the main analysis:
   
   "python main.py"

3. Run the dashboard:
   
   "python dashboard.py"

📁 Project Structure

- data/ — Dataset files
- charts/ — Generated visualizations and dashboard
- main.py — Data analysis and chart generation
- dashboard.py — Combined music dashboard
- README.md — Project documentation

🏁 Conclusion

This project demonstrates how Python can be used to analyze a large music dataset and convert numerical information into meaningful visualizations. It helps identify patterns and trends in music characteristics across different genres.