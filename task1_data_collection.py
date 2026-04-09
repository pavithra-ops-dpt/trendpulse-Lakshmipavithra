import requests
import time
import json
import os
from datetime import datetime


TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


HEADERS = {"User-Agent": "TrendPulse/1.0"}


CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"],
}


def get_category(title):
    if not title:
        return None
    t = title.lower()
    for cat, words in CATEGORIES.items():
        for w in words:
            if w in t:
                return cat
    return None


def get_story(story_id):
    try:
        url = ITEM_URL.format(story_id)
        
        r = requests.get(url, headers=HEADERS)
        if r.status_code == 200:
            return r.json()
    except:
        pass
    return None


def main():
    
    try:
        r = requests.get(TOP_URL, headers=HEADERS)
        top_ids = r.json()[:100]
    except:
        print("Error getting top story IDs")
        return

    results = []
    count_per_cat = {c: 0 for c in CATEGORIES}
    

    
    for cat in CATEGORIES:
        time.sleep(2)  

        for sid in top_ids:
            if count_per_cat[cat] >= 25:
                break

            story = get_story(sid)
            if not story:
                continue

            title = story.get("title", "")
            detected = get_category(title)

            if detected == cat:
                item = {
                    "post_id": story.get("id"),
                    "title": title,
                    "category": cat,
                    "score": story.get("score"),
                    "num_comments": story.get("descendants"),
                    "author": story.get("by"),
                    "collected_at": datetime.now().isoformat()
                }
                results.append(item)
                count_per_cat[cat] += 1

    
    os.makedirs("data", exist_ok=True)
    fname = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

    with open(fname, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved to: {fname}")
    print("Total stories collected:", len(results))

main()




