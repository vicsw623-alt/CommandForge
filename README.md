# ⚙️ CmdForge

A lightweight Python-based command management system that lets you **store, manage, and execute custom commands dynamically** using JSON.

---

## 🚀 Overview

CmdForge allows you to:

* Define custom commands with Python code
* Store them persistently in a JSON file
* Execute them on demand
* Manage (delete/reset) commands easily

Think of it as a **simple macro / command execution engine** built with Python.

---

## 📁 Project Structure

```
project/
│── main.py        # Main program
│── data.json      # Command storage (auto-created)
│── Code.py        # Optional: predefined safe functions
```

---

## ⚙️ How It Works

* Commands are stored in `data.json` as:

```json
[
    {
        "cmd": "example",
        "code": "print('Hello')"
    }
]
```

* The program:

  1. Parses user input
  2. Saves commands
  3. Executes code using `exec()`

---

## 🧪 Usage

Run the program:

```bash
python main.py
```

---

### 1️⃣ Add a Command

```
set.<command>:<python_code>
```

Example:

```
set.hello:print("Hello World")
```

---

### 2️⃣ Run a Command

```
run.<command>
```

Example:

```
run.hello
```

Output:

```
hello 실행
Hello World
```

---

### 3️⃣ Delete a Command

```
del.<command>
```

---

### 4️⃣ Delete All Commands

```
delall
```

---

### 5️⃣ Exit Program

```
end
```

---

## ⚠️ Important Notes

### 🔥 Use of `exec()`

This program executes raw Python code using `exec()`.

* This means **any code will run as-is**
* It can be dangerous if misused

👉 Recommended for:

* Personal use
* Learning / experimentation

👉 Not recommended for:

* Untrusted input
* Production environments

---

## 🧠 Core Functions

* `setcmd()` → Parses and saves commands
* `runcmd()` → Executes stored commands
* `delcmd()` → Deletes specific command
* `delallcmd()` → Clears all commands
* `read_data_from_file()` → Loads JSON data

---

## 💡 Possible Improvements

* Restrict execution to safe functions (via `Code.py`)
* Prevent duplicate commands
* Add `list` command to view all stored commands
* Replace `exec()` with safer execution logic

---

## 📌 Summary

> CmdForge is a simple but powerful tool for creating and executing custom Python commands on the fly.

---

## 🛠 Requirements

* Python 3.x

---

## 📄 License

This project is for educational purposes. Use at your own risk.

---