# CommandForge

CommandForge is a simple Python-based CLI tool that allows you to create, manage, and execute custom commands stored in a JSON file.

## Features

* Create custom commands with Python code
* Execute saved commands
* Delete specific commands
* Modify existing commands
* View command details
* List all commands
* Reset all stored commands

## Requirements

* Python 3.x
* No external libraries required (uses built-in `json` and `os`)

## How It Works

All commands are stored in a file named `data.json`. Each command consists of:

```json
{
    "cmd": "command_name",
    "code": "python_code"
}
```

## Usage

Run the script:

```bash
python main.py
```

Then use the following commands in the CLI:

### Create a Command

```
set.<cmd>:<code>
```

Example:

```
set.hello:print("Hello World")
```

### Run a Command

```
run.<cmd>
```

Example:

```
run.hello
```

### Delete a Command

```
del.<cmd>
```

Example:

```
del.hello
```

### Modify a Command

```
mod.<cmd>:<code>
```

* Deletes the existing command and replaces it with new code

Example:

```
mod.hello:print("Hello again")
```

### Show Command Code

```
show.<cmd>
```

### List All Commands

```
list
```

### Delete All Commands

```
delall
```

### Help

```
help
```

or

```
?
```

### Exit Program

```
end
```

## Error Handling

* If `data.json` does not exist, it will be automatically created.
* Duplicate commands are not allowed.
* If a command fails during execution:

  * `NameError` is handled separately and may prompt deletion.
  * Other exceptions will display error type and details.

## Notes

* Commands are executed using Python's `exec()` function.
* Be cautious: running arbitrary code can be dangerous.

## File Structure

```
.
├── main.py
└── data.json
```

## Future Improvements (Optional Ideas)

* Add command validation before saving
* Safer execution environment (sandboxing)
* Command descriptions
* Export/import commands

---

Enjoy building your own command system with CommandForge!
