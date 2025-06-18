import streamlit as st
import csv
import re
import pandas as pd
from io import StringIO, BytesIO

def filter_and_merge_rows(input_csv_content):
    input_rows = list(csv.reader(StringIO(input_csv_content)))
    days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

    # Step 1: Filter out rows until the first valid weekday appears
    filtered_rows = []
    start_processing = False

    for row in input_rows:
        if row and any(re.match(f"^{day}\\b", row[0].strip()) for day in days):
            start_processing = True
        if start_processing:
            filtered_rows.append(row)

    # Step 2: Merge rows that do NOT start with a weekday into the last valid row
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

    # Step 3: Replace consecutive commas with a single comma
    cleaned_rows = []
    for row in merged_rows:
        row_string = ",".join(row)
        row_string = re.sub(r",+", ",", row_string)
        cleaned_rows.append(row_string.split(','))

    # Step 4: Process dates and merge times
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

        if len(merged_row) > 5:
            field5 = merged_row[4]
            extra_text = merged_row[5:]

            contains_day = any(re.match(f"^{d}\\b", field.strip()) for d in days for field in extra_text)
            contains_date = any(re.match(r"\d{1,2}\.\d{1,2}", field.strip()) for field in extra_text)
            contains_endet = any("endet" in field.lower() for field in extra_text)

            if contains_day or contains_date or contains_endet:
                merged_row = merged_row[:5]
            else:
                merged_row[3] = merged_row[3] + " " + " ".join(extra_text)
                merged_row = merged_row[:5]

        # Enclose the fourth field (index 3) in double quotes if it exists
        if len(merged_row) > 3:
            merged_row[3] = f'"{merged_row[3]}"'
            
        updated_rows.append(merged_row)

    output_csv = StringIO()
    writer = csv.writer(output_csv)
    writer.writerows(updated_rows)
    return output_csv.getvalue()

# Streamlit UI
st.title("CSV Processor and Downloader")

# File upload
uploaded_file = st.file_uploader("Upload a CSV or TXT file", type=["csv", "txt"])

if uploaded_file is not None:
    file_content = uploaded_file.getvalue().decode("utf-8")
    
    # Process file
    processed_csv_content = filter_and_merge_rows(file_content)

    # Convert to DataFrame for preview
    df = pd.read_csv(StringIO(processed_csv_content), header=None)

    st.write("### Processed Data Preview:")
    st.dataframe(df)

    # Convert to bytes for download
    output_bytes = BytesIO(processed_csv_content.encode("utf-8"))
    
    # Download button
    st.download_button(
        label="Download Processed CSV",
        data=output_bytes,
        file_name="processed_output.csv",
        mime="text/csv"
    )
