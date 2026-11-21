import sqlite3
from datetime import datetime

DB_NAME = "study_tracker.db"


def init_db():
    """Initialize SQLite database and seed initial schedule tasks if empty."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            title TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending',
            completed_at TEXT
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM tasks")
    if cursor.fetchone()[0] == 0:
        initial_tasks = [
            ("Today (Setup)", "Set up SQL environment & GitHub repo"),
            ("Today (Setup)", "Gather B.Com Sem 5-6 syllabus & past papers"),
            ("Today (Setup)", "Queue 20 Japanese flashcards & Aptitude bookmark"),
            ("Today (Setup)", "Dinner by 8 PM, alarm at 5:15 AM, lights out 9:45 PM"),
            ("Week 1", "Sun: First 5:15 AM Brahma Muhurta session + 10 SQL queries"),
            ("Week 1", "Wed: Start Python + SQL Expense/GST Analyzer project"),
            ("Week 1", "Fri: Push documented Project 1 code to GitHub"),
            ("Week 1", "Sat: 1 timed B.Com past paper & 1-hr Aptitude mini-mock"),
        ]
        cursor.executemany(
            "INSERT INTO tasks (category, title) VALUES (?, ?)",
            initial_tasks,
        )
        conn.commit()

    conn.close()


def view_tasks():
    """Display all tasks grouped by status and category."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, title, status, completed_at FROM tasks ORDER BY id")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("\nNo tasks found.")
        return

    print("\n" + "=" * 72)
    print(f"{'ID':<4} | {'Status':<8} | {'Category':<15} | {'Task'}")
    print("-" * 72)
    for task_id, category, title, status, completed_at in rows:
        mark = "[x]" if status == "Done" else "[ ]"
        print(f"{task_id:<4} | {mark:<8} | {category:<15} | {title}")
    print("=" * 72)


def mark_done():
    """Mark a task as completed with a timestamp."""
    view_tasks()
    try:
        task_id = int(input("\nEnter Task ID to mark as Done: ").strip())
    except ValueError:
        print("Invalid input. Please enter a numeric Task ID.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute(
        "UPDATE tasks SET status = 'Done', completed_at = ? WHERE id = ?",
        (timestamp, task_id),
    )

    if cursor.rowcount == 0:
        print(f"No task found with ID {task_id}.")
    else:
        conn.commit()
        print(f"Task #{task_id} marked as Done at {timestamp}!")

    conn.close()


def add_task():
    """Add a new custom task to the tracker."""
    category = input("Enter Category (e.g., B.Com, SQL, Japanese, Aptitude): ").strip()
    title = input("Enter Task Description: ").strip()

    if not category or not title:
        print("Category and description cannot be empty.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (category, title) VALUES (?, ?)",
        (category, title),
    )
    conn.commit()
    conn.close()
    print(f"Added task: [{category}] {title}")


def show_progress():
    """Calculate and display completion stats."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'Done'")
    done = cursor.fetchone()[0]
    conn.close()

    pct = (done / total * 100) if total > 0 else 0
    bar_length = 25
    filled = int(bar_length * done // total) if total > 0 else 0
    bar = "#" * filled + "-" * (bar_length - filled)

    print(f"\nOverall Progress: [{bar}] {done}/{total} ({pct:.1f}%)")


def main():
    init_db()
    while True:
        print("\n--- Brahma Muhurta & Career Prep Tracker ---")
        print("1. View All Tasks")
        print("2. Mark Task as Done")
        print("3. Add New Task")
        print("4. View Progress Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            mark_done()
        elif choice == "3":
            add_task()
        elif choice == "4":
            show_progress()
        elif choice == "5":
            print("Keep up the consistency! Goodbye.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()