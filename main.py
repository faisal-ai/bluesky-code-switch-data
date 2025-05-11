import json
import csv
import os
from bluesky.fetcher import BlueskyFetcher

'''def save_posts(posts, filename='data/bluesky_posts.json'):
    """
    Save collected posts to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print(f"💾 Saved {len(posts)} posts to {filename}")
'''

def save_posts(posts, filename="data/bluesky_posts.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Define the CSV columns
    fieldnames = [
        "uri",
        "text",
        "language",
        "created_at",
        "author_handle",
        "author_display_name",
        "external_link"
    ]

    # Write to CSV
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts)

    print(f"✅ Saved {len(posts)} posts to {filename}")


def main():
    handle = 'fayysal.bsky.social'
    app_password = 'dckj-gzaf-ocrr-zavc'

    fetcher = BlueskyFetcher(handle, app_password)
    posts = fetcher.fetch_posts(query='a', max_posts=10)
    save_posts(posts)

if __name__ == '__main__':
    main()