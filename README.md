# CSV Outlier Removal Tool

## Overview

The **CSV Outlier Removal Tool** is a Python application designed to simplify one of the most important steps in data preprocessing: identifying and removing outliers from numerical data.

Outliers can distort statistical analysis, reduce the accuracy of machine learning models, and lead to misleading insights. This project automates the process by allowing users to select any CSV file, detect outliers in numerical columns, and generate a cleaned dataset ready for further analysis.

## Features

* Select any CSV file using a graphical file picker
* Automatically detects numerical columns
* Identifies and removes statistical outliers
* Generates a cleaned CSV file
* Easy-to-use interface with no hardcoded file paths
* Suitable for data analysis and machine learning preprocessing

## Technologies Used

* Python
* Pandas
* NumPy
* Tkinter

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/csv-outlier-removal-tool.git
```

Navigate to the project directory:

```bash
cd csv-outlier-removal-tool
```

Install the required libraries:

```bash
pip install pandas numpy
```

## Usage

1. Run the Python script.
2. Select the CSV file you wish to clean.
3. The program detects numerical columns and removes statistical outliers.
4. A cleaned CSV file is generated and saved for further analysis.

## Why This Project?

Data cleaning is a fundamental step in every data science workflow. Removing outliers helps improve data quality, making statistical analysis and machine learning models more reliable.

This project was built to strengthen my understanding of:

* Data preprocessing
* Statistical analysis
* File handling in Python
* Building reusable data processing tools

## Example Workflow

```
Select CSV
      ↓
Read Dataset
      ↓
Detect Numerical Columns
      ↓
Identify Outliers
      ↓
Remove Outliers
      ↓
Export Cleaned CSV
```

---

## Author

**Azma Awaiz**

I'm continuously building projects in Python, data analytics, machine learning, and quantitative finance to strengthen my technical skills and create practical tools for real-world data problems.

If you have any suggestions or feedback, feel free to connect with me on LinkedIn or explore my other repositories.
