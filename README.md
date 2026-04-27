# CommandForge

CommandForge is a simple CLI-based command manager written in Python.
It allows you to create, store, execute, and manage custom commands using a JSON file.

---

## 📌 Features

* Create custom commands with Python code
* Store commands in a JSON file (`data.json`)
* Execute saved commands dynamically
* Delete individual commands or all commands
* View stored commands and their code
* List all available commands

---

## ⚙️ Requirements

* Python 3.x

---

## 🚀 Usage

Run the program:

```bash
python main.py
```

---

## 🧩 Commands

### 1. Create a command

```
set.<cmd>:<code>
```

Example:

```
set.hello:print("Hello World")
```

---

### 2. Run a command

```
run.<cmd>
```

Example:

```
run.hello
```

---

### 3. Delete a command

```
del.<cmd>
```

Example:

```
del.hello
```

---

### 4. Delete all commands

```
delall
```

---

### 5. Show command code

```
show.<cmd>
```

Example:

```
show.hello
```

---

### 6. List all commands

```
list
```

---

### 7. Help

```
help
```

or

```
?
```

---

### 8. Exit program

```
end
```

---

## 📂 Data Storage

All commands are stored in:

```
data.json
```

Format example:

```json
[
    {
        "cmd": "hello",
        "code": "print(\"Hello World\")"
    }
]
```

---

## ⚠️ Notes

* Commands execute using Python's `exec()` function.
* Invalid Python code may cause errors during execution.
* Be cautious when running unknown or unsafe code.

---

## 🛠️ Future Improvements (Optional Ideas)

* Command editing feature
* Command categories
* Safer execution environment
* Command import/export

---

## 📖 Summary

CommandForge is a lightweight tool for experimenting with dynamic command execution in Python.
It is useful for learning, prototyping, and building simple command systems.
