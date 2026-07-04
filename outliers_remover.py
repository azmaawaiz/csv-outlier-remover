import os
import platform
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# 1. Function to open a file dialog cleanly
def choose_file_dialog(initial_dir):
    root = Tk()
    root.withdraw()       # Hide the main small window
    root.lift()           # Force it to bring the file explorer to the top
    root.attributes('-topmost', True) # Keep it on top of the terminal
    
    filename = askopenfilename(
        initialdir=initial_dir,
        title="Select the CSV file",
        filetypes=[("CSV files", "*.csv")]
    )
    root.destroy()        # Cleanly close the window manager instance
    return filename

csv_filename = choose_file_dialog(".")

if not csv_filename or not os.path.exists(csv_filename):
    print(f"Error: No file was selected or found.")
    exit()

try:
    df = pd.read_csv(csv_filename)
    print(f"\nSuccessfully loaded '{os.path.basename(csv_filename)}'.")
    print(f"Initial Shape: {df.shape}")
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

def remove_outliers_iqr(file_path, output_path):
    numerical_cols = [
        'Annual_Income', 'Debt_to_Income_Ratio', 'Employment_Length_Years',
        'Credit_Lines_Outstanding', 'Loan_Amount', 'FICO_Score',
        'Previous_Delinquencies', 'Loan_Term_Months', 'Interest_Rate_%'
    ]
    
    initial_rows = df.shape[0]
    mask = pd.Series(True, index=df.index)
    
    for col in numerical_cols:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            mask = mask & (df[col] >= lower_bound) & (df[col] <= upper_bound)
            
            outliers_count = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
            if outliers_count > 0:
                print(f"  - Found {outliers_count} outliers in '{col}'")
    
    df_clean = df[mask]
    df_clean.to_csv(output_path, index=False)
    
    removed_rows = initial_rows - df_clean.shape[0]
    print(f"\nOutlier removal complete!")
    print(f"Rows before: {initial_rows} | Rows after: {df_clean.shape[0]} ({removed_rows} removed)")
    print(f"Cleaned dataset saved directly to: '{output_path}'")

# --- EXECUTION & PATH ROUTING ---

# Automatically routes output to the active user's system Downloads folder
home_dir = os.path.expanduser("~")
downloads_folder = os.path.join(home_dir, "Downloads")
output_filename = os.path.join(downloads_folder, 'cleaned_consumer_lending.csv')

# Run cleaning
remove_outliers_iqr(csv_filename, output_filename)

# --- DETECT OS & CHOOSE CORRECT WINDOW MANAGER ---
print("\nLaunching Excel...")
try:
    if platform.system() == 'Windows':
        os.startfile(output_filename) # Works perfectly on Windows
    elif platform.system() == 'Darwin':  # macOS
        os.system(f'open "{output_filename}"') # FIXED: Changed from startfile to system
    else:  # Linux
        os.system(f'xdg-open "{output_filename}"') # FIXED: Changed from startfile to system
except Exception as e:
    print(f"Could not open file automatically: {e}")

print("="*40)
print("Excel file has been requested to open.")
print("="*40)
    
# Keep code running/prompt user 
while True:
    user_choice = input("Do you want to end the Python code? (yes/no): ").strip().lower()
    
    if user_choice in ['yes', 'y', '']:
        print("\nExiting script. Goodbye!")
        break  
    elif user_choice in ['no', 'n']:
        print("\nKeeping script active. Press Ctrl+C in this window later to force quit.")
        input("Press [ENTER] whenever you are finally ready to close the program...")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")