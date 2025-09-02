# 🚀 Python Beginners Project – Tutorial 3

Welcome to **Python Beginners Project**! 🎉  
This tutorial series now covers up to **working with CSV files**.

---

## 📂 Project Structure

```
python-beginners/
├── .github/
│   └── workflows/
│       └── python-app.yml   # GitHub Actions workflow
├── simple_example.py        # Tutorial 1: Basics
├── file_example.py          # Tutorial 2: Files
├── csv_example.py           # Tutorial 3: CSV Files
└── README.md                # Instructions
```

---

## ▶️ How to Run Locally

1. Make sure you have **Python 3.10+** installed.  
2. Navigate to the project folder in terminal:

```bash
cd path/to/python-beginners
```
3. Run the CSV example script:

```bash
python csv_example.py
```

4. Check the newly created `students.csv` in the folder.  
5. Observe the output printed in the terminal.

---

## 📖 What You’ll Learn

### Tutorial 1 (simple_example.py)
- Taking user input  
- Printing messages  

### Tutorial 2 (file_example.py)
- Creating a new text file  
- Writing lines to a file (`w`)  
- Appending lines to a file (`a`)  
- Reading the file content (`r`)  
- Counting lines and basic text manipulation  

### Tutorial 3 (csv_example.py)
- Writing tabular data into a CSV file  
- Appending rows  
- Reading CSVs with `csv.reader`  
- Reading CSVs as dictionaries (`csv.DictReader`) for easy column access  

---

## 🤖 GitHub Actions CI/CD

The workflow automatically runs all three tutorials on every push to main.

---

### **GitHub Actions workflow** (`python-app.yml`)  

```yaml
name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Run simple_example.py
      run: python simple_example.py <<< "World"

    - name: Run file_example.py
      run: python file_example.py

    - name: Run csv_example.py
      run: python csv_example.py
```

Happy learning Python! ❤️
