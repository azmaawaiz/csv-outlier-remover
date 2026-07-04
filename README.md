# CSV Outlier Removal Tool

A Python application that automates outlier detection and removal from CSV datasets using the **Interquartile Range (IQR)** method. The tool is designed to simplify data preprocessing by allowing users to select a dataset through a graphical interface, clean it, and automatically generate a new CSV file ready for analysis.

## 📖 Overview

Outliers can have a significant impact on statistical analysis, visualization, and machine learning models. This project provides an automated solution for identifying and removing extreme values from numerical financial data while maintaining a simple and user-friendly workflow.

Unlike many scripts that require hardcoded file paths, this application allows users to select any CSV file through a built-in file explorer and automatically saves the cleaned dataset to the user's Downloads folder.

## ✨ Features

* 📂 Graphical file picker (no hardcoded file paths)
* 📊 Detects outliers using the **Interquartile Range (IQR)** method
* 🔍 Processes multiple numerical financial columns automatically
* 📈 Reports the number of outliers detected in each column
* 🧹 Removes outliers while preserving the original dataset
* 💾 Automatically exports a cleaned CSV file
* 🚀 Opens the cleaned dataset after processing
* ⚠️ Includes file validation and error handling
* 💻 Compatible with Windows, macOS, and Linux

## 📁 Supported Columns

The application currently processes the following numerical columns:

* Annual Income
* Debt-to-Income Ratio
* Employment Length
* Credit Lines Outstanding
* Loan Amount
* FICO Score
* Previous Delinquencies
* Loan Term (Months)
* Interest Rate

## 🛠 Technologies Used

* Python
* Pandas
* Tkinter
* OS & Platform libraries

## ⚙️ How It Works

1. Launch the application.
2. Select a CSV file using the graphical file explorer.
3. The program validates the selected file.
4. The IQR method is applied to each supported numerical column.
5. Outliers are identified and removed.
6. A cleaned CSV file is created in the Downloads folder.
7. The cleaned dataset is opened automatically.

## 📊 Outlier Detection Method

This project uses the **Interquartile Range (IQR)** method to detect outliers.

For each numerical column:

* Calculate the first quartile (Q1)
* Calculate the third quartile (Q3)
* Compute the Interquartile Range (IQR = Q3 − Q1)
* Define:

  * Lower Bound = Q1 − 1.5 × IQR
  * Upper Bound = Q3 + 1.5 × IQR
* Any value outside these bounds is treated as an outlier and removed.

The IQR method is widely used because it is robust against skewed data and does not assume a normal distribution.

## 🚀 Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/csv-outlier-removal-tool.git
```

Navigate to the project directory:

```bash
cd csv-outlier-removal-tool
```

Install the required dependency:

```bash
pip install pandas
```

Run the application:

```bash
python outlier_removal.py
```

## 📂 Output

After processing, the application:

* Creates a cleaned CSV file named **cleaned_consumer_lending.csv**
* Saves it to your **Downloads** folder
* Automatically opens the cleaned file
* Displays a summary including:

  * Original row count
  * Final row count
  * Number of removed records
  * Outliers detected per column

## 👨‍💻 Why I Built This Project

This project was created to strengthen my skills in:

* Data preprocessing
* Statistical analysis
* Python automation
* Cross-platform development
* File handling
* Building user-friendly data science tools

The goal was not only to implement the IQR algorithm but also to create a practical application that improves the user experience by eliminating hardcoded file paths, automating file management, and providing informative feedback throughout the data-cleaning process.

## 📄 License

This project is available under the MIT License.
