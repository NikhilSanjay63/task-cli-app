#!/usr/bin/env python3
import sys
import json
import datetime

# 1. Gracefully handle missing commands
if len(sys.argv) < 2:
    print("Usage: task-cli [command] [arguments]")
    sys.exit()

action = sys.argv[1]

# 2. Safely load existing tasks as a Dictionary
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = {} # Initialize as an empty dictionary

# 3. Route the commands

if action == "add":
    if len(sys.argv) < 3:
        print("Error: Please provide a description.")
        sys.exit()
        
    # Calculate new ID based on dictionary keys
    if len(tasks) == 0:
        new_id = "1"
    else:
        highest_id = max([int(key) for key in tasks.keys()])
        new_id = str(highest_id + 1)
        
    # Create the task inside the dictionary using the ID as the key
    tasks[new_id] = {
        "description": sys.argv[2],
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
    }
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        
    print(f"Task added successfully (ID: {new_id})")

elif action == "list":
    # Check if a filter was provided
    filter_status = sys.argv[2] if len(sys.argv) == 3 else None
    
    # .items() gives us the ID (key) and the data (value) at the same time
    for task_id, task_data in tasks.items():
        if filter_status is None or task_data["status"] == filter_status:
            print(f"{task_id} - {task_data['description']} [{task_data['status']}]")

elif action == "update":
    if len(sys.argv) < 4:
        print("Error: Please provide both an ID and a new description.")
        sys.exit()
        
    task_id = sys.argv[2]
    new_description = sys.argv[3]
    
    # Instant lookup - no for loop needed!
    if task_id in tasks:
        tasks[task_id]['description'] = new_description
        tasks[task_id]['updatedAt'] = datetime.datetime.now().isoformat()
        
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print(f"Task {task_id} updated successfully.")
    else:
        print(f"Error: Task {task_id} not found.")

elif action == "delete":
    if len(sys.argv) < 3:
        print("Error: Please provide an ID to delete.")
        sys.exit()
        
    task_id = sys.argv[2]
    
    if task_id in tasks:
        del tasks[task_id] # Instant deletion
        
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Error: Task {task_id} not found.")

elif action == "mark-in-progress":
    if len(sys.argv) < 3:
        print("Error: Please provide an ID.")
        sys.exit()
        
    task_id = sys.argv[2]
    
    if task_id in tasks:
        tasks[task_id]['status'] = "in-progress"
        tasks[task_id]['updatedAt'] = datetime.datetime.now().isoformat()
        
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print(f"Task {task_id} marked as in-progress.")
    else:
        print(f"Error: Task {task_id} not found.")

elif action == "mark-done":
    if len(sys.argv) < 3:
        print("Error: Please provide an ID.")
        sys.exit()
        
    task_id = sys.argv[2]
    
    if task_id in tasks:
        tasks[task_id]['status'] = "done"
        tasks[task_id]['updatedAt'] = datetime.datetime.now().isoformat()
        
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print(f"Task {task_id} marked as done.")
    else:
        print(f"Error: Task {task_id} not found.")

else:
    print(f"Unknown command: {action}")