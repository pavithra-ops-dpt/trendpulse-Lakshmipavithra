
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Load the analysed data
df = pd.read_csv("data/trends_analysed.csv")
os.makedirs("outputs", exist_ok=True)

# 1. Chart for Top Stories (by score)
top_stories = df.sort_values("score", ascending=False).head(10)
# Prepare titles for plotting, shortening if necessary
plot_titles = [title[:50] + "..." if len(title) > 50 else title for title in top_stories["title"]]

plt.figure(figsize=(10, 6))
plt.barh(plot_titles, top_stories["score"], color='skyblue') # Using barh for horizontal bars
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis() # To have the highest score at the top
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close() # Close the figure to free memory

# 2. Chart for Category Distribution
category_counts = df["category"].value_counts()
categories = category_counts.index
counts = category_counts.values
# A simple list of colors or default matplotlib colors
your_color_list = plt.get_cmap('tab10', len(categories)) # Using a colormap for distinct colors

plt.figure(figsize=(8, 5))
plt.bar(categories, counts, color=your_color_list.colors)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Story Distribution by Category")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# 3. Scatter plot (e.g., Score vs. Number of Comments, colored by category)
x = df["score"]
y = df["num_comments"]
# To get colors based on category, we need to map categories to numerical values for matplotlib
# Or, use a categorical scatter plot if categories are few
# For simplicity, let's just make a basic scatter plot for now
colors = df['category'].astype('category').cat.codes # Map categories to numbers for coloring
cmap = plt.get_cmap('viridis', len(df['category'].unique())) # Colormap for categories

plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, c=colors, cmap=cmap, alpha=0.7)
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs. Number of Comments")
cbar = plt.colorbar(scatter, ticks=range(len(df['category'].unique())),
             label='Category')
cbar.set_ticklabels(df['category'].unique())
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()



print("All charts and dashboard saved in /outputs")
