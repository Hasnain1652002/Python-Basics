import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import csv
import re
import pandas as pd
from io import StringIO

def filter_and_merge_rows(input_csv_content):
    # Function to process and merge rows based on the content
    input_rows = list(csv.reader(StringIO(input_csv_content)))
    days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

    filtered_rows = []
    start_processing = False

    for row in input_rows:
        if row and any(re.match(f"^{day}\\b", row[0].strip()) for day in days):
            start_processing = True
        if start_processing:
            filtered_rows.append(row)

    merged_rows = []
    current_row = None

    for row in filtered_rows:
        if row and any(re.match(f"^{day}\\b", row[0].strip()) for day in days):
            if current_row:
                merged_rows.append(current_row)
            current_row = row
        else:
            if current_row:
                current_row.extend(row)

    if current_row:
        merged_rows.append(current_row)

    cleaned_rows = []
    for row in merged_rows:
        row_string = ",".join(row)
        row_string = re.sub(r",+", ",", row_string)
        cleaned_rows.append(row_string.split(','))

    updated_rows = []
    for row in cleaned_rows:
        if len(row) > 3:
            if re.match(r"\d{1,2}\.\d{1,2}$", row[1]) and re.match(r"\d{1,2}\.\d{1,2}$", row[2]):
                row[1] += ".2025"
                row[2] += ".2025"

            time_fields = [i for i, v in enumerate(row) if re.match(r"\d{2}:\d{2}", v)]
            if len(time_fields) >= 2:
                row[1] = f"{row[1]} {row[time_fields[0]]}"
                row[2] = f"{row[2]} {row[time_fields[1]]}"
                for index in sorted(time_fields, reverse=True):
                    del row[index]

        row = [field for field in row if not re.match(r"N - \d+/\d+", field)]
        row = [field for field in row if field.strip()]

        merged_row = []
        for field in row:
            if field.startswith(" ") and merged_row:
                merged_row[-1] += " " + field.strip()
            else:
                merged_row.append(field)
        # step 5 
        if len(merged_row) > 5:
            extra_text = merged_row[5:]

            # Check if extra fields contain a date or time
            contains_date_or_time = any(
                re.match(r"\d{1,2}\.\d{1,2}\.\d{4}", field.strip()) or  # Matches dates like 08.11.2024
                re.match(r"\d{1,2}:\d{2}", field.strip())  # Matches time like 10:36
                for field in extra_text
            )

            if contains_date_or_time:
                # Remove everything after 5th field
                merged_row = merged_row[:5]
            else:
                # Otherwise, merge extra text into column 4
                merged_row[3] += " " + " ".join(extra_text)
                merged_row = merged_row[:5]


        if len(merged_row) > 3:
            merged_row[3] = merged_row[3].strip('"')  # Remove existing quotes to prevent duplication
            merged_row[3] = f'"{merged_row[3]}"'  # Ensure only single pair of quotes


        updated_rows.append(merged_row)

    output_csv = StringIO()
    writer = csv.writer(output_csv, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(updated_rows)
    return output_csv.getvalue()

def open_csv_file():
    # Allow CSV file selection
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()
        
        processed_csv_content = filter_and_merge_rows(file_content)
        global processed_data
        processed_data = processed_csv_content
        df = pd.read_csv(StringIO(processed_csv_content), header=None)
        display_table(df)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file: {e}")

def open_text_file():
    # Allow Text file selection
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()
        
        # If it's a .txt file, convert to CSV-like format by splitting rows
        if file_path.endswith('.txt'):
            file_content = '\n'.join([line.strip() for line in file_content.splitlines() if line.strip()])

        processed_csv_content = filter_and_merge_rows(file_content)
        global processed_data
        processed_data = processed_csv_content
        df = pd.read_csv(StringIO(processed_csv_content), header=None)
        display_table(df)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    if not processed_data:
        messagebox.showwarning("Warning", "No processed data to save!")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    
    try:
        # Save the processed CSV content
        with open(file_path, "w", encoding="utf-8", newline='') as file:
            file.write(processed_data)
        
        # Open the saved file and replace triple quotes with single quotes
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        content = content.replace('"""', '"')  # Replace triple quotes with single quotes
        
        # Write the cleaned content back with newline='' to prevent blank lines
        with open(file_path, "w", encoding="utf-8", newline='') as file:
            file.write(content)

        messagebox.showinfo("Success", "File saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")


def display_table(df):
    for widget in frame_table.winfo_children():
        widget.destroy()
    tree = ttk.Treeview(frame_table, show="headings")
    tree["columns"] = list(df.columns)
    
    for col in df.columns:
        tree.heading(col, text=f"Column {col+1}")
        tree.column(col, width=120)
    
    # Customize table background color
    style = ttk.Style()
    style.configure("Treeview", background="#1f2a44", foreground="white", fieldbackground="#1f2a44")
    style.configure("Treeview.Heading", background="#3c4a69", font=("Arial", 10, "bold"), foreground="white")
    
    for _, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))
    
    tree.pack(fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("CSV Converter")
root.state('zoomed')
root.configure(bg='black')  # Set background to black

heading_label = tk.Label(root, text="CSV Converter", font=("Arial", 24, "bold"), bg="black", fg="white")
heading_label.pack(pady=10)

btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=10)

# Buttons to upload CSV and text files
open_csv_button = tk.Button(btn_frame, text="📂 Upload CSV", command=open_csv_file, width=20, bg="#008CBA", fg="white", font=("Arial", 12, "bold"))
open_csv_button.pack(side=tk.LEFT, padx=10)

open_text_button = tk.Button(btn_frame, text="📂 Upload Text", command=open_text_file, width=20, bg="#008CBA", fg="white", font=("Arial", 12, "bold"))
open_text_button.pack(side=tk.LEFT)

frame_table = tk.Frame(root, bg="black")
frame_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

save_button = tk.Button(root, text="💾 Download Processed CSV", command=save_file, width=25, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
save_button.pack(pady=10)

processed_data = ""
root.mainloop()
