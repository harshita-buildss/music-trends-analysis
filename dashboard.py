import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/spotify-tracks.csv")
df = df.dropna(subset=["artists", "album_name", "track_name"])
df = df.drop_duplicates()
df["duration_min"] = df["duration_ms"] / 60000

# Create dashboard
fig, axes = plt.subplots(3, 2, figsize=(16, 13))

fig.suptitle(
    "SPOTIFY MUSIC TRENDS DASHBOARD",
    fontsize=20,
    fontweight="bold"
)

# 1. Popularity by genre
pop = df.groupby("track_genre")["popularity"].mean().nlargest(10).sort_values()
axes[0, 0].barh(pop.index, pop.values, color="#55C2A3")
axes[0, 0].set_title("Top 10 Popular Genres")
axes[0, 0].set_xlabel("Average Popularity")

# 2. Energy by genre
energy = df.groupby("track_genre")["energy"].mean().nlargest(10).sort_values()
axes[0, 1].barh(energy.index, energy.values, color="#E6A15C")
axes[0, 1].set_title("Top 10 Highest Energy Genres")
axes[0, 1].set_xlabel("Average Energy")

# 3. Popularity distribution
axes[1, 0].hist(df["popularity"], bins=20, color="#8E7CC3", edgecolor="white")
axes[1, 0].set_title("Popularity Distribution")
axes[1, 0].set_xlabel("Popularity Score")
axes[1, 0].set_ylabel("Number of Tracks")

# 4. Danceability vs Energy
axes[1, 1].scatter(
    df["danceability"], df["energy"],
    alpha=0.15, s=5, color="#E07A9A"
)
axes[1, 1].set_title("Danceability vs Energy")
axes[1, 1].set_xlabel("Danceability")
axes[1, 1].set_ylabel("Energy")

# 5. Average song duration
duration = df.groupby("track_genre")["duration_min"].mean().nlargest(10).sort_values()
axes[2, 0].barh(duration.index, duration.values, color="#65A6D8")
axes[2, 0].set_title("Top 10 Genres by Song Duration")
axes[2, 0].set_xlabel("Duration (Minutes)")

# 6. Explicit vs Non-Explicit
counts = df["explicit"].value_counts().reindex([False, True])
axes[2, 1].pie(
    counts.values,
    labels=["Non-Explicit", "Explicit"],
    autopct="%1.1f%%",
    colors=["#8E7CC3", "#E6A15C"],
    startangle=90
)
axes[2, 1].set_title("Explicit vs Non-Explicit Songs")

# Final layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig(
    "charts/music_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()