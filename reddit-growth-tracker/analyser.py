import pandas as pd
import numpy as np

CSV_FILE = "post_history.csv"
OUTPUT_FILE = "growth_analysis.txt"

def calculate_metrics(group):
"""
Calculate growth metrics for one post.
"""

```
group = group.sort_values("snapshot_number")

scores = group["score"].tolist()

first_score = scores[0]
final_score = scores[-1]

absolute_growth = final_score - first_score

if first_score == 0:
    growth_rate = 0
else:
    growth_rate = (
        (final_score - first_score)
        / first_score
    ) * 100

increments = []

for i in range(1, len(scores)):
    increments.append(
        scores[i] - scores[i - 1]
    )

if len(increments) >= 2:
    acceleration = (
        increments[-1]
        - increments[0]
    )
else:
    acceleration = 0

consistency = np.std(increments) if increments else 0

return {
    "title": group.iloc[0]["title"],
    "final_score": final_score,
    "absolute_growth": absolute_growth,
    "growth_rate": growth_rate,
    "acceleration": acceleration,
    "consistency": consistency
}
```

def analyse_posts():

```
df = pd.read_csv(CSV_FILE)

results = []

grouped = df.groupby("post_id")

for post_id, group in grouped:

    if len(group) < 2:
        continue

    metrics = calculate_metrics(group)

    metrics["post_id"] = post_id

    results.append(metrics)

return pd.DataFrame(results)
```

def identify_patterns(results):

```
fastest_growth = results.loc[
    results["growth_rate"].idxmax()
]

most_consistent = results.loc[
    results["consistency"].idxmin()
]

early_peaker = results.loc[
    results["acceleration"].idxmin()
]

late_accelerator = results.loc[
    results["acceleration"].idxmax()
]

return (
    fastest_growth,
    most_consistent,
    early_peaker,
    late_accelerator
)
```

def save_analysis(
fastest_growth,
most_consistent,
early_peaker,
late_accelerator):

```
report = []

report.append("=" * 60)
report.append("REDDIT POST GROWTH ANALYSIS")
report.append("=" * 60)

report.append("\nFASTEST GROWTH\n")
report.append(
    f"Title: {fastest_growth['title'][:60]}"
)
report.append(
    f"Final Score: {fastest_growth['final_score']}"
)
report.append(
    f"Growth Rate: {fastest_growth['growth_rate']:.2f}%"
)

report.append("\nMOST CONSISTENT\n")
report.append(
    f"Title: {most_consistent['title'][:60]}"
)
report.append(
    f"Consistency Score: {most_consistent['consistency']:.2f}"
)

report.append("\nEARLY PEAKER\n")
report.append(
    f"Title: {early_peaker['title'][:60]}"
)
report.append(
    f"Acceleration: {early_peaker['acceleration']:.2f}"
)

report.append("\nLATE ACCELERATOR\n")
report.append(
    f"Title: {late_accelerator['title'][:60]}"
)
report.append(
    f"Acceleration: {late_accelerator['acceleration']:.2f}"
)

content = "\n".join(report)

with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
) as file:

    file.write(content)

print(content)
```

def main():

```
results = analyse_posts()

if results.empty:
    print("No data available.")
    return

(
    fastest_growth,
    most_consistent,
    early_peaker,
    late_accelerator
) = identify_patterns(results)

save_analysis(
    fastest_growth,
    most_consistent,
    early_peaker,
    late_accelerator
)
```

if **name** == "**main**":
main()
