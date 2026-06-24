import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "post_history.csv"
OUTPUT_IMAGE = "score_trajectories.png"

def load_data():
return pd.read_csv(CSV_FILE)

def calculate_metrics(df):

```
metrics = []

grouped = df.groupby("post_id")

for post_id, group in grouped:

    group = group.sort_values(
        "snapshot_number"
    )

    scores = group["score"].tolist()

    if len(scores) < 2:
        continue

    first_score = scores[0]
    final_score = scores[-1]

    growth_rate = 0

    if first_score > 0:
        growth_rate = (
            (final_score - first_score)
            / first_score
        ) * 100

    increments = []

    for i in range(1, len(scores)):
        increments.append(
            scores[i] - scores[i - 1]
        )

    consistency = (
        pd.Series(increments).std()
        if increments
        else 0
    )

    metrics.append({
        "post_id": post_id,
        "title": group.iloc[0]["title"],
        "growth_rate": growth_rate,
        "consistency": consistency
    })

return pd.DataFrame(metrics)
```

def identify_highlights(metrics):

```
fastest_growth = metrics.loc[
    metrics["growth_rate"].idxmax()
]

most_consistent = metrics.loc[
    metrics["consistency"].idxmin()
]

return (
    fastest_growth["post_id"],
    most_consistent["post_id"]
)
```

def generate_chart():

```
df = load_data()

metrics = calculate_metrics(df)

fastest_growth_id, most_consistent_id = (
    identify_highlights(metrics)
)

plt.figure(figsize=(14, 8))

grouped = df.groupby("post_id")

for post_id, group in grouped:

    group = group.sort_values(
        "snapshot_number"
    )

    title = (
        group.iloc[0]["title"][:40]
    )

    linewidth = 1.5
    marker = "o"

    if post_id == fastest_growth_id:

        linewidth = 4
        marker = "s"

    elif post_id == most_consistent_id:

        linewidth = 4
        marker = "^"

    plt.plot(
        group["snapshot_number"],
        group["score"],
        label=title,
        linewidth=linewidth,
        marker=marker
    )

plt.title(
    "Post Score Trajectories - r/technology"
)

plt.xlabel(
    "Time (30-min intervals)"
)

plt.ylabel(
    "Score"
)

plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    OUTPUT_IMAGE,
    dpi=150
)

print(
    f"Saved {OUTPUT_IMAGE}"
)
```

if **name** == "**main**":
generate_chart()
