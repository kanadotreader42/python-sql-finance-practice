\# Study \& Career Prep CLI Tracker



A lightweight, persistent command-line task and habit tracker built with \*\*Python\*\* and \*\*SQLite\*\*. Designed to organize daily study blocks across university coursework, technical skill-building (SQL \& Python), language learning (Japanese), and competitive aptitude preparation.



\---



\## Features



\- \*\*SQLite Persistence:\*\* Automatically initializes a local `study\\\_tracker.db` database to store tasks, categories, statuses, and completion timestamps.

\- \*\*Pre-Seeded Workflow:\*\* Populates starter setup and weekly milestones on first launch.

\- \*\*Task Management:\*\* View tasks in a formatted CLI table, add custom study items by category, and mark tasks as completed with automatic timestamps.

\- \*\*Progress Tracking:\*\* Displays an ASCII progress bar and live completion percentage.

\- \*\*Zero External Dependencies:\*\* Runs purely on Python's built-in `sqlite3` and `datetime` modules.



\---



\## Project Structure



```text

bcom-finance-sql-python/

├── tracker.py          # Main CLI application and SQLite database logic

├── .gitignore          # Excludes local SQLite database files from version control

└── README.md           # Project documentation


