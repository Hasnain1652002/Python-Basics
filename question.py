import PyPDF2
import re
import json

# Open the PDF file in read mode
pdf_file = open('questions.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Get the total number of pages in the PDF file
num_pages = pdf_reader.getNumPages()

# Define a regular expression pattern to match question and answer strings
pattern = r"Q\d+\.\s(.+)\n\s+(a\.\s.+\n\s+b\.\s.+\n\s+c\.\s.+\n\s+d\.\s.+)"

# Loop through each page of the PDF file
questions = []
for page in range(num_pages):
    # Extract the text from the current page
    page_text = pdf_reader.getPage(page).extractText()

    # Find all matches of the pattern in the page text
    matches = re.findall(pattern, page_text)

    # Loop through each match and extract the question and answers
    for match in matches:
        question = match[0]
        answers = match[1].split('\n')[1:-1]

        # Create a dictionary for the current question and answers
        q_dict = {
            "question": question,
            "answers": answers,
            "correctAnswer": 0
        }

        # Add the dictionary to the list of questions
        questions.append(q_dict)

# Convert the list of questions to a JSON string
json_str = json.dumps(questions)

# Print the JSON string to the console
print(json_str)
