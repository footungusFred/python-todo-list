import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("  No tasks yet!")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "⬜"
        print(f"  {i}. {status} {t['title']}")

def main():
    tasks = load_tasks()
    print("=== Todo List Manager ===")
    print("Commands: add | done <n> | remove <n> | list | quit
")

    while True:
        cmd = input("> ").strip()
        if not cmd:
            continue
        parts = cmd.split(maxsplit=1)
        action = parts[0].lower()

        if action == "quit":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        elif action == "add":
            if len(parts) < 2:
                print("Usage: add <task title>")
            else:
                tasks.append({"title": parts[1], "done": False})
                print(f"  Added: {parts[1]}")
                save_tasks(tasks)
        elif action == "list":
            list_tasks(tasks)
        elif action == "done":
            try:
                idx = int(parts[1]) - 1
                tasks[idx]["done"] = True
                print(f"  Marked done: {tasks[idx]['title']}")
                save_tasks(tasks)
            except (IndexError, ValueError):
                print("  Invalid task number.")
        elif action == "remove":
            try:
                idx = int(parts[1]) - 1
                removed = tasks.pop(idx)
                print(f"  Removed: {removed['title']}")
                save_tasks(tasks)
            except (IndexError, ValueError):
                print("  Invalid task number.")
        else:
            print("  Unknown command.")

if __name__ == "__main__":
    main()
