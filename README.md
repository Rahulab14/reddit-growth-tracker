# 🚀 Reddit Post Growth Tracker

A Python-based analytics tool that tracks Reddit post engagement over time, calculates growth metrics, identifies content performance patterns, and visualizes post score trajectories.


---

# 📌 Project Overview

Social media engagement is time-dependent.

A post that gains traction immediately behaves differently from one that accelerates later.

This application:

- Collects Reddit post snapshots every 30 minutes
- Stores engagement history in CSV format
- Calculates growth metrics
- Detects engagement patterns
- Generates trajectory visualizations
- Produces a human-readable analysis report

---


# 🛠️ Tech Stack

- Python 3
- Requests
- Pandas
- Matplotlib
- Reddit Public JSON API

---

# 📂 Project Structure

```text
reddit-growth-tracker/

├── tracker.py
├── analyser.py
├── visualiser.py

├── post_history.csv
├── growth_analysis.txt
├── score_trajectories.png

├── requirements.txt
├── README.md
├── .gitignore

└── screenshots/
    └── dashboard.png
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/rahulab14/reddit-growth-tracker.git

cd reddit-growth-tracker
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Dependencies

```text
requests
pandas
matplotlib
apscheduler
```

---

# 🌐 Reddit API

This project uses Reddit's public JSON API.

Example endpoint:

```text
https://www.reddit.com/r/technology/top.json?limit=10&t=day
```

User-Agent header:

```text
growth-tracker/1.0 (by /u/student)
```

No authentication is required.

---

# 📊 Subreddit Used

```text
r/technology
```

---

# ▶️ Running The Tracker

Run:

```bash
python tracker.py
```

The tracker:

- Fetches Top 10 posts
- Stores score and comment count
- Records timestamps
- Saves snapshots to CSV

---

# 📁 Output File

## post_history.csv

Generated automatically.

Columns:

```csv
post_id,title,score,num_comments,timestamp,snapshot_number
```

Example:

```csv
p1,AI models that run on low-end hardware,320,45,2026-06-25T09:00:00,1
```

---

# 📈 Growth Analysis

Run:

```bash
python analyser.py
```

Generates:

```text
growth_analysis.txt
```

---

# Growth Metrics

## 1. Absolute Growth

Formula:

```text
Final Score - Initial Score
```

Example:

```text
4620 - 320

= 4300
```

---

## 2. Growth Rate %

Formula:

```text
((Final Score - Initial Score) / Initial Score) × 100
```

Example:

```text
((4620 - 320) / 320) × 100

= 1343.75%
```

---

## 3. Acceleration

Measures whether growth is speeding up or slowing down.

Formula:

```text
Last Interval Growth - First Interval Growth
```

---

## 4. Consistency Score

Uses standard deviation of growth increments.

Lower value = more consistent growth.

---

# 🎯 Pattern Identification

The system automatically identifies:

---

## Fastest Growth

Highest growth rate percentage.

Example:

```text
AI models that run on low-end hardware
```

---

## Most Consistent

Lowest growth variation.

Example:

```text
Why Python is still the best first language
```

---

## Early Peaker

Strong early growth but slows down later.

Example:

```text
Docker vs Podman: Which one to use?
```

---

## Late Accelerator

Growth increases significantly in later snapshots.

Example:

```text
OpenAI unveils new GPT-4o update
```

---

# 📊 Visualisation

Run:

```bash
python visualiser.py
```

Generates:

```text
score_trajectories.png
```

---

# Chart Features

- 10 separate post lines
- Snapshot tracking
- Growth comparison
- Highlighted fastest-growth post
- Highlighted most-consistent post
- PNG output
- 150 DPI export

---

# Chart Information

X Axis:

```text
Time (30-minute intervals)
```

Y Axis:

```text
Score
```

Title:

```text
Post Score Trajectories - r/technology (25/06/2026)
```

---

# 📄 Sample Analysis Output

```text
============================================================
REDDIT POST GROWTH ANALYSIS
============================================================

FASTEST GROWTH

Title: AI models that run on low-end hardware
Final Score: 4620
Growth Rate: 134.50%

MOST CONSISTENT

Title: Why Python is still the best first language
Consistency Score: 5.21

EARLY PEAKER

Title: Docker vs Podman: Which one to use?
Acceleration: -15.30

LATE ACCELERATOR

Title: OpenAI unveils new GPT-4o update
Acceleration: 42.90
```

---

# 📋 Development Mode

For faster testing:

Inside `tracker.py`

```python
TEST_MODE = True
```

Uses:

```text
5-second intervals
```

instead of:

```text
30-minute intervals
```

---

# Production Configuration

Set:

```python
TEST_MODE = False
```

This enables:

```text
7 snapshots
30-minute intervals
3-hour tracking window
```

Required by the assessment.

---

# 🔍 Findings From Actual Run

Subreddit:

```text
r/technology
```

Observations:

- AI-related posts showed the strongest growth.
- Python educational content had the most stable engagement.
- Some posts experienced rapid early growth and plateaued.
- OpenAI-related news accelerated significantly during later intervals.
- Technology announcements generated the highest comment counts.

---

# 🧪 Files Generated

| File | Purpose |
|--------|----------|
| post_history.csv | Snapshot history |
| growth_analysis.txt | Growth metrics report |
| score_trajectories.png | Visualization chart |

---

# 🚧 Limitations

- Uses Reddit public API only.
- Posts may leave the Top 10 during tracking.
- No database persistence.
- Data collection depends on subreddit activity.

---
