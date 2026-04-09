import numpy as np

df["category"].value_counts()
#print(df["category"].value_counts())
idx = df["num_comments"].idxmax()
df.loc[idx, "title"]
df.loc[idx, "num_comments"]

print("Most commented story title:", df.loc[idx, "title"])
print("Number of comments:", df.loc[idx, "num_comments"])

df["engagement"] = df["num_comments"] / (df["score"] + 1)
#print(df[["title", "engagement"]].head())
avg_score = df["score"].mean()
df["is_popular"] = df["score"] > avg_score

print("Average score:", avg_score)
#print(df[["title", "score", "is_popular"]].head())

scores = df["score"].values # Define scores array from the 'score' column
print("Mean score:", np.mean(scores))
print("Median score:", np.median(scores))
print("Max score:", np.max(scores))

df.to_csv("data/trends_analysed.csv", index=False)
print("Saved to data/trends_analysed.csv")
