import pandas as pd
import os
from datetime import datetime

# Get today's date in the correct format for the filename
today_date = datetime.now().strftime('%Y%m%d')
file_path = f"data/trends_{today_date}.json"
if not os.path.exists(file_path):
    print(f"Error: File {file_path} not found. Please ensure data collection ran successfully.")
    
    file_path = "data/trends_20260406.json" 
    if not os.path.exists(file_path):
        print(f"Error: Fallback file {file_path} also not found.")
        df = pd.DataFrame() 
    else:
        df = pd.read_json(file_path)
else:
    df = pd.read_json(file_path)




print("Loaded rows:", len(df))
df.drop_duplicates(subset="post_id", inplace=True)
df.dropna(subset=["post_id", "title", "score"], inplace=True)
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].fillna(0).astype(int)
df = df[df["score"] >= 5]
df["title"] = df["title"].str.strip()
print("After removing duplicates:", len(df))
df.to_csv("data/trends_clean.csv", index=False)
print(df["category"].value_counts())
