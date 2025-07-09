import csv
import re
from io import StringIO

def filter_and_merge_rows(input_csv_content):
    input_rows = list(csv.reader(StringIO(input_csv_content)))
    days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    
    # Step 1: Filter out rows until the first valid weekday appears
    filtered_rows = []
    start_processing = False

    for row in input_rows:
        if row and any(re.match(f"^{day}\\b", row[0].strip()) for day in days):
            start_processing = True  # Start collecting rows from this point
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
            # Update date format
            if re.match(r"\d{1,2}\.\d{1,2}$", row[1]) and re.match(r"\d{1,2}\.\d{1,2}$", row[2]):
                row[1] += ".2025"
                row[2] += ".2025"

            # Find time fields dynamically and merge them with dates
            time_fields = [i for i, v in enumerate(row) if re.match(r"\d{2}:\d{2}", v)]
            if len(time_fields) >= 2:
                row[1] = f"{row[1]} {row[time_fields[0]]}"
                row[2] = f"{row[2]} {row[time_fields[1]]}"
                for index in sorted(time_fields, reverse=True):
                    del row[index]  # Remove separate time fields

        # Step 5: Remove fields matching the pattern "N - 0162/6231597" (phone numbers with "N -")
        row = [field for field in row if not re.match(r"N - \d+/\d+", field)]

        # Step 6: Remove blank fields
        row = [field for field in row if field.strip()]

        # Step 7: Merge fields that start with a space into the previous field
        merged_row = []
        for field in row:
            if field.startswith(" ") and merged_row:
                merged_row[-1] += " " + field.strip()
            else:
                merged_row.append(field)
        
        # Step 8: Process field 5 condition
        if len(merged_row) > 5:  
            field5 = merged_row[4]  # FD1, FD2, etc.
            extra_text = merged_row[5:]  

            # Check if extra_text contains a weekday, date, or 'endet'
            contains_day = any(re.match(f"^{d}\\b", field.strip()) for d in days for field in extra_text)
            contains_date = any(re.match(r"\d{1,2}\.\d{1,2}", field.strip()) for field in extra_text)
            contains_endet = any("endet" in field.lower() for field in extra_text)

            if contains_day or contains_date or contains_endet:
                merged_row = merged_row[:5]  # Keep only up to field5
            else:
                merged_row[3] = merged_row[3] + " " + " ".join(extra_text)  # Append extra text to field4
                merged_row = merged_row[:5]  # Trim row after field5
        
        updated_rows.append(merged_row)

    # Convert the final rows back to a CSV string
    output_csv = StringIO()
    writer = csv.writer(output_csv)
    writer.writerows(updated_rows)
    return output_csv.getvalue()

# Example input CSV as a string
input_csv = """,Bautzen ,,,,,
Abrufzeitraum: 01.10.2024-01.01.2025,,,,,,
Dienstplan: Dienstplan Q4/2024,,,,,,
Zeitraum: 01.10.2024 - 31.10.2024,,,,,,
Tag,Datum,endet,Arzt,Notfallnummer,Dienst,
,Zeit,am/um,,,,
Di,1.1,2.1,"Dr. med. Stehr, Christiane",N - 0162/6231597,FD1 (Nacht),
,19:00,07:00,,,,
Mi,2.1,2.1,"Dr. med. Weiß, Stefan",N - 0162/4043037,FD1 (Tag),
,14:00,19:00,,,,
Mi,2.1,2.1,Medizinisches,N - 03591/3632920,SD Bautzen,
,15:00,19:00,Versorgungszentrum Bautzen,,,
,,,in Trägerschaft der,,,
,,,Medizinischen,,,
,,,Versorgungszentren der,,,
,,,Oberlausitz gGmbH,,,
Mi,2.1,3.1,"PD Dr.med.habil. Speiser,",N - 0171/3101541,FD1 (Nacht),
,19:00,07:00,Uwe,,,
Do,3.1,3.1,"Dr. med. Liebner, Raphael",N - 0152/53104802,FD1 (Tag),
,07:00,19:00,,,,
Do,3.1,3.1,"Dr. med. Hanisch, Anke",N - 0160/3627613,SD Bautzen,
,09:00,13:00,,,,
Do,3.1,3.1,Medizinisches,,SD Bischofswerda,
,09:00,13:00,Versorgungszentrum am,,,
,,,Universitätsklinikum Carl,,,
,,,Gustav Carus Dresden GmbH,,,
Do,3.1,3.1,"Dr. med. Reiche, Anna",N - 0179/9101218,FD2,
,09:00,21:00,,,,
Do,3.1,3.1,"Dr. med. Stehr, Christiane",N - 0162/6231597,SD Bautzen,
,15:00,19:00,,,,
Do,3.1,4.1,"Dipl.-Med. Eckert, Frank",N - 0174/6333951,FD1 (Nacht),
,19:00,07:00,,,,
Fr,4.1,4.1,"Boeck, Cornelia",N - 0173/6568366,FD1 (Tag),
,07:00,19:00,,,,
Fr,4.1,4.1,"Dr. med. Rentzsch, Jörn",N - 0173/7246126,SD Bautzen,
,09:00,13:00,,,,
,,,,,06.08.2024 12:48,Seite 1/26
Bautzen,,,,,,
Tag,Datum,endet,Arzt,Notfallnummer,Dienst,
,Zeit,am/um,,,,
Fr,4.1,4.1,"Dr. med. Pfeifer, Carsten",N - 0172/9977552,SD Bischofswerda,
,09:00,13:00,,,,
Fr,4.1,4.1,"Dr. med. Tschötsch, Susanne",N - 0174/5766841,FD2,
,09:00,21:00,,,,
"""

# Process the input CSV using the function
output_csv = filter_and_merge_rows(input_csv)
print(output_csv)
