import streamlit as st
import csv
import io
import re
from datetime import datetime

def process_file(uploaded_file):
    content = uploaded_file.read().decode('utf-8')
    lines = content.split('\n')

    # Extract end year from Abrufzeitraum
    abruf_line = next(line for line in lines if line.startswith('Abrufzeitraum:'))
    date_range = abruf_line.split(': ')[1].strip()
    _, end_date_str = date_range.split('-')
    end_date = datetime.strptime(end_date_str, '%d.%m.%Y')
    end_year = end_date.year

    # Step 1: Skip until weekday line
    step1_lines = []
    found = False
    for line in lines:
        stripped = line.strip()
        if not found:
            if re.match(r'^(Mo|Di|Mi|Do|Fr|Sa|So),', stripped):
                found = True
                step1_lines.append(stripped)
        else:
            step1_lines.append(stripped)

    # Step 2: Merge continuation lines
    step2_lines = []
    current = None
    for line in step1_lines:
        stripped = line.strip()
        if re.match(r'^(Mo|Di|Mi|Do|Fr|Sa|So),', stripped):
            if current:
                step2_lines.append(current)
            current = stripped
        else:
            current = f"{current} {stripped}" if current else stripped
    if current:
        step2_lines.append(current)

    # Step 3: Collapse commas
    step3_lines = [re.sub(r',+', ',', line).strip(',') for line in step2_lines]

    # CSV parsing and processing
    processed = []
    for line in step3_lines:
        with io.StringIO(line) as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            try:
                row = next(reader)
            except:
                continue
            
            if len(row) < 7:
                continue

            try:
                # Step 4: Process dates
                start = f"{row[1]}.{end_year} {row[5]}"
                end = f"{row[2]}.{end_year} {row[6]}"
                new_row = [row[0], start, end, row[3], row[4]]
                
                # Step 5: Handle remaining fields
                if len(row) > 5:
                    remaining = row[7:]
                    if any('Tag,Datum,endet' in field for field in remaining):
                        new_row = new_row[:5]
                    else:
                        new_row[3] += ' ' + ' '.join(remaining).strip()
                        new_row = new_row[:5]
                
                processed.append(new_row)
            except IndexError:
                continue

    # Generate output CSV
    output = io.StringIO()
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(processed)
    return output.getvalue()

# Streamlit UI
st.title('Dienstplan CSV Converter')
uploaded_file = st.file_uploader("Upload Dienstplan CSV", type=['csv', 'txt'])

if uploaded_file:
    try:
        result = process_file(uploaded_file)
        st.download_button(
            label="Download Processed CSV",
            data=result,
            file_name="processed.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")