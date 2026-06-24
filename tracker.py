import requests
import csv
import time
from datetime import datetime

SUBREDDIT = "technology"

CSV_FILE = "post_history.csv"

TOTAL_SNAPSHOTS = 7

INTERVAL_SECONDS = 1800

TEST_MODE = True

if TEST_MODE:
    INTERVAL_SECONDS = 5


def fetch_top_posts():
    """
    Fetch top 10 posts from Reddit.
    """

    url = f"https://www.reddit.com/r/{SUBREDDIT}/top.json?limit=10&t=day"

    headers = {
        "User-Agent": "growth-tracker/1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    posts = []

    for item in data["data"]["children"]:

        post = item["data"]

        posts.append({
            "post_id": post["id"],
            "title": post["title"],
            "score": post["score"],
            "num_comments": post["num_comments"]
        })

    return posts









def initialize_csv():
    """
    Create CSV with headers.
    """

    with open(
            CSV_FILE,
            mode="w",
            newline="",
            encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "post_id",
            "title",
            "score",
            "num_comments",
            "timestamp",
            "snapshot_number"
        ])


def save_snapshot(posts, snapshot_number):
    """
    Append snapshot data.
    """

    timestamp = datetime.now().isoformat()

    with open(
            CSV_FILE,
            mode="a",
            newline="",
            encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        for post in posts:

            writer.writerow([
                post["post_id"],
                post["title"],
                post["score"],
                post["num_comments"],
                timestamp,
                snapshot_number
            ])


def run_tracker():

    initialize_csv()

    print(f"Tracking r/{SUBREDDIT}")

    for snapshot in range(1, TOTAL_SNAPSHOTS + 1):

        print(f"\nSnapshot {snapshot}")

        try:

            posts = fetch_top_posts()

            save_snapshot(
                posts,
                snapshot
            )

            print(
                f"Saved {len(posts)} posts"
            )

        except Exception as error:

            print(
                f"Error: {error}"
            )

        if snapshot < TOTAL_SNAPSHOTS:

            print(
                f"Waiting {INTERVAL_SECONDS} seconds..."
            )

            time.sleep(
                INTERVAL_SECONDS
            )

    print("\nTracking completed")


if __name__ == "__main__":
    run_tracker()