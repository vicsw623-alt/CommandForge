좋아, 지금 코드 기준으로 보면 기능이 꽤 정리돼 있어서 README도 그에 맞게 구조 잡아주는 게 맞다. 핵심 기능들을 정확히 반영해서 깔끔한 영어 README 만들어줄게.

---

# CommandForge

CommandForge is a simple Python-based CLI tool that allows you to create, store, and execute custom commands using a JSON file.

## Features

* Create custom commands with Python code
* Execute stored commands dynamically
* Delete specific commands or all commands
* View stored command code
* List and manage commands through a simple CLI interface
* Automatic JSON file creation if it does not exist
* Duplicate command prevention

## How It Works

Commands are stored in a `data.json` file in the following format:

```json
[
    {
        "cmd": "example",
        "code": "print('Hello World')"
    }
]
```

Each command consists of:

* `cmd`: the command name
* `code`: the Python code executed when the command runs

## Usage

### Create a Command

```
set.<cmd>:<code>
```

Example:

```
set.hello:print("Hello World")
```

---

### Run a Command

```
run.<cmd>
```

Example:

```
run.hello
```

---

### Delete a Command

```
del.<cmd>
```

Example:

```
del.hello
```

---

### Delete All Commands

```
delall
```

---

### Show Command Code

```
show.<cmd>
```

Example:

```
show.hello
```

---

### Help Menu

```
help
```

or

```
?
```

---

### Exit Program

```
end
```

## Error Handling

* If a command does not exist:

  ```
  there is no cmd(<cmd>)
  ```

* If a command already exists:

  ```
  This command already exists
  ```

* If execution fails due to invalid code:

  * The error type and details are displayed
  * Option to delete the faulty command is provided

## Notes

* Commands are executed using Python's `exec()` function
  → Only use trusted code to avoid security risks

* The program automatically creates `data.json` if it does not exist

## Requirements

* Python 3.x

## File Structure

```
project/
│── main.py
│── data.json (auto-created)
│── Code.py (optional predefined commands)
```

## Future Improvements (Optional Ideas)

* Command listing feature (`list`)
* Command editing
* Safer execution environment (sandboxing)
* Command categories or tags

---