# task-cli

A small, file-based command line task manager written in Python.

## Features

- Add tasks with timestamps
- List tasks with optional status filtering
- Update task descriptions
- Delete tasks by ID
- Mark tasks as `in-progress` or `done`
- Stores tasks in a local `tasks.json` file

## Requirements

- Python 3.7+

## Installation

1. Clone or download this repository.
2. Ensure Python is installed and available on your PATH.
3. Run the CLI directly with Python:

```sh
python task_cli.py <command> [options]
```

On Windows, the included `task-cli.bat` wrapper can also be used:

```bat
task-cli <command> [options]
```

## Usage

```sh
python task_cli.py <command> [arguments]
```

### Commands

- `add <description>`
  - Add a new task.
  - Example: `python task_cli.py add "Buy groceries"`

- `list [status]`
  - Show all tasks, or only tasks matching a status.
  - Supported statuses: `todo`, `in-progress`, `done`
  - Example: `python task_cli.py list` or `python task_cli.py list todo`

- `update <task_id> <description>`
  - Change the description of an existing task.
  - Example: `python task_cli.py update 1 "Buy groceries and milk"`

- `delete <task_id>`
  - Remove a task by its ID.
  - Example: `python task_cli.py delete 1`

- `mark-in-progress <task_id>`
  - Set a task status to `in-progress`.
  - Example: `python task_cli.py mark-in-progress 1`

- `mark-done <task_id>`
  - Set a task status to `done`.
  - Example: `python task_cli.py mark-done 1`

## Data storage

Tasks are stored in `tasks.json` in the same directory as the script. Each task is saved as an object keyed by ID.

Example entry:

```json
{
  "1": {
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-06-20T12:00:00",
    "updatedAt": "2026-06-20T12:00:00"
  }
}
```

## Development

- Keep CLI logic in `task_cli.py`.
- Use `argparse` for argument validation and help text.
- Handle invalid JSON in `tasks.json` gracefully.

## Notes

- Task IDs are generated automatically.
- The CLI preserves task order by numeric ID when listing.
- Use multi-word descriptions by wrapping them in quotes.

## License

This project is provided as-is. Modify and use it freely.
