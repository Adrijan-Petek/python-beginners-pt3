# 🚀 Python Beginners Project – Tutorial 3

Welcome to **Python Beginners Project – Tutorial 3**! 🎉  
This tutorial series now includes **working with CSV files** while continuing to reinforce basics from previous tutorials.

[![GitHub stars](https://img.shields.io/github/stars/Adrijan-Petek/python-beginners-pt3?style=social)](https://github.com/Adrijan-Petek/python-beginners-pt3/stargazers)
[![Workflow Status](https://github.com/Adrijan-Petek/python-beginners-pt3/actions/workflows/python-app.yml/badge.svg)](https://github.com/Adrijan-Petek/python-beginners-pt3/actions/workflows/python-app.yml)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)

---

## 📂 Project Structure

```plaintext
python-beginners/
├── .github/
│   └── workflows/
│       └── python-app.yml   # GitHub Actions workflow
├── simple_example.py        # Tutorial 1: Basics
├── file_example.py          # Tutorial 2: Files
├── csv_example.py           # Tutorial 3: CSV Files
└── README.md                # Project instructions
````

---

## ▶️ Step 1: Prerequisites

* Python **3.10+**

  ```bash
  python --version
  ```
* Git (for cloning repository)

  ```bash
  git --version
  ```

---

## ▶️ Step 2: Clone the Repository

```bash
git clone https://github.com/Adrijan-Petek/python-beginners-pt3.git
cd python-beginners-pt3
```

---

## ▶️ Step 3: Run the CSV Example

```bash
python csv_example.py
```

This will:

1. Create a CSV file `students.csv`
2. Write tabular student data
3. Append additional rows
4. Read and display data in two ways:

   * Using `csv.reader`
   * Using `csv.DictReader` for easy column access

**Example terminal output:**

```plaintext
Name,Age,Grade
Alice,20,A
Bob,22,B
Charlie,21,A-
Number of students: 3
Student Names: ['Alice', 'Bob', 'Charlie']
```

You can also open `students.csv` in your folder to see the tabular data.

---

## 🌟 What You’ll Learn

### Tutorial 1 – `simple_example.py`

* Taking user input
* Printing messages

### Tutorial 2 – `file_example.py`

* Creating a new text file
* Writing lines (`w`)
* Appending lines (`a`)
* Reading file content (`r`)
* Counting lines

### Tutorial 3 – `csv_example.py`

* Writing tabular data into a CSV file
* Appending rows
* Reading CSVs with `csv.reader`
* Reading CSVs as dictionaries (`csv.DictReader`) for easy column access

---

## 🤖 GitHub Actions CI/CD

Workflow runs **all three tutorials** automatically on every push to `main`:

* `.github/workflows/python-app.yml`
* Ensures scripts run correctly
* Beginner-friendly introduction to CI/CD automation

---

## 💡 Tips

* Modify `csv_example.py` to add more students or columns.
* Practice reading only specific columns using `DictReader`.
* Extend the workflow to run tests or validate CSV content.

---

## ❤️ Contribute

Open issues, submit pull requests, or **star the repo** ⭐

[Visit the GitHub repository »](https://github.com/Adrijan-Petek/python-beginners-pt3)

````
