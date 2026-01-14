import requests
import pandas as pd
import time

GITHUB_TOKEN = ""
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

def fetch_repos(topic, limit=20):
    """ Fetches repositories for a specific topic """
    url = f"https://api.github.com/search/repositories?q=topic:{topic}&sort=stars&per_page={limit}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f"Error fetching {topic}: {response.status_code}")
        return []
    
# 1. Harvest data
topics = ['machine-learning', 'blockchain', 'biotech', 'fintech', 'web3']
all_repos = []

print("Starting data extraction...")

for topic in topics:
    print(f"Fetching {topic} startups")
    items = fetch_repos(topic, limit=20)

    for item in items:
        all_repos.append({
            'name': item['name'],
            'full_name': item['full_name'],
            'description': item['description'],
            'topics': item['topics'],
            'stars': item['stargazers_count'],
            'url': item['html_url']
        })
    time.sleep(1)

# 2. Save data
df = pd.DataFrame(all_repos)

# Drop rows where description is missing
df = df.dropna(subset=['description'])

df.to_csv("github_startups.csv", index=False)
print(f"Success! Saved {len(df)} startups to csv")
print(df.head())