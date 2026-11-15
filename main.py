import pandas as pd

# Load the Spotify dataset
df = pd.read_csv("data/spotify-tracks.csv")

# Display basic information
print("MUSIC TRENDS DATA ANALYSIS")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nColumn Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
# DATA CLEANING

print("\n--- DATA CLEANING ---")

# Check duplicate records
print("Duplicate rows:", df.duplicated().sum())

# Remove rows with missing important information
df = df.dropna(subset=["artists", "album_name", "track_name"])

# Remove duplicate records
df = df.drop_duplicates()

# Convert duration from milliseconds to minutes
df["duration_min"] = df["duration_ms"] / 60000

print("Dataset after cleaning:", df.shape)

print("\nRemaining missing values:")
print(df.isnull().sum().sum())

print("\nCleaning completed successfully!")
# BASIC MUSIC STATISTICS

print("\n--- MUSIC STATISTICS ---")

# Total number of songs
print("Total Songs:", len(df))

# Number of unique genres
print("Total Genres:", df["track_genre"].nunique())

# Average popularity
print("Average Popularity:", round(df["popularity"].mean(), 2))

# Most popular genres by average popularity
print("\nTop 10 Genres by Average Popularity:")

genre_popularity = df.groupby("track_genre")["popularity"].mean()

print(genre_popularity.sort_values(ascending=False).head(10))

# Most energetic genres
print("\nTop 10 Genres by Average Energy:")

genre_energy = df.groupby("track_genre")["energy"].mean()

print(genre_energy.sort_values(ascending=False).head(10))

# Average song duration
print("\nAverage Song Duration:")
print(round(df["duration_min"].mean(), 2), "minutes")
import matplotlib.pyplot as plt

# TOP 10 POPULAR GENRES

top_genres = (
    df.groupby("track_genre")["popularity"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_genres.index,
    top_genres.values,
    color="#55C2A3"
)

plt.title("Top 10 Most Popular Music Genres",
          fontsize=15, fontweight="bold")

plt.xlabel("Average Popularity")
plt.ylabel("Music Genre")

plt.tight_layout()

plt.savefig("charts/top_genres_popularity.png",
            dpi=300, bbox_inches="tight")

plt.show()
# TOP 10 HIGHEST ENERGY GENRES

top_energy = (
    df.groupby("track_genre")["energy"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_energy.index,
    top_energy.values,
    color="#E6A15C"
)

plt.title("Top 10 Highest Energy Music Genres",
          fontsize=15, fontweight="bold")

plt.xlabel("Average Energy")
plt.ylabel("Music Genre")

plt.tight_layout()

plt.savefig("charts/top_energy_genres.png",
            dpi=300, bbox_inches="tight")

plt.show()
# MUSIC POPULARITY DISTRIBUTION

plt.figure(figsize=(10, 6))

plt.hist(
    df["popularity"],
    bins=20,
    color="#8E7CC3",
    edgecolor="white"
)

plt.title("Distribution of Music Popularity",
          fontsize=15, fontweight="bold")

plt.xlabel("Popularity Score")
plt.ylabel("Number of Tracks")

plt.tight_layout()

plt.savefig("charts/popularity_distribution.png",
            dpi=300, bbox_inches="tight")

plt.show()
# CHART 04: DANCEABILITY VS ENERGY

plt.figure(figsize=(10, 6))

plt.scatter(
    df["danceability"],
    df["energy"],
    alpha=0.15,
    s=8,
    color="#E07A9A"
)

plt.title("Danceability vs Energy",
          fontsize=15, fontweight="bold")

plt.xlabel("Danceability")
plt.ylabel("Energy")

plt.tight_layout()

plt.savefig("charts/danceability_vs_energy.png",
            dpi=300, bbox_inches="tight")

plt.show()
# CHART 05: AVERAGE SONG DURATION BY GENRE

genre_duration = (
    df.groupby("track_genre")["duration_min"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    genre_duration.index,
    genre_duration.values,
    color="#65A6D8"
)

plt.title("Top 10 Genres by Average Song Duration",
          fontsize=15, fontweight="bold")

plt.xlabel("Average Duration (Minutes)")
plt.ylabel("Music Genre")

plt.tight_layout()

plt.savefig("charts/average_duration_by_genre.png",
            dpi=300, bbox_inches="tight")

plt.show()
# CHART 06: EXPLICIT VS NON-EXPLICIT SONGS

explicit_counts = df["explicit"].value_counts().sort_index()

labels = ["Non-Explicit", "Explicit"]

plt.figure(figsize=(8, 6))

plt.pie(
    explicit_counts.values,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#8E7CC3", "#E6A15C"],
    explode=[0, 0.05],
    shadow=True
)

plt.title("Explicit vs Non-Explicit Songs",
          fontsize=15, fontweight="bold")

plt.tight_layout()

plt.savefig("charts/explicit_vs_non_explicit.png",
            dpi=300, bbox_inches="tight")

plt.show()