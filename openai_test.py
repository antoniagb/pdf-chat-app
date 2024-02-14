from openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
import PyPDF2
import json

# Laden Sie die Umgebungsvariablen aus der .env-Datei
load_dotenv()

'''# Define the path to your Excel file
excel_file_path = '/Users/thiennguyen/Desktop/uni/Master/3. Semester/AA Analytische Anwendungen/Passport Ranking.xlsx'

# Read the Excel file into a pandas DataFrame
data = pd.read_excel(excel_file_path)'''



# PDF-Dokument öffnen
with open('/Users/thiennguyen/Desktop/uni/Master/3. Semester/BI Projekt Business Intelligence/Employer Branding ist eine strategische Maßnahme der Personalabteilung.pdf', 'rb') as pdf_file:
    # PDF-Reader-Objekt erstellen
    reader = PyPDF2.PdfReader(pdf_file)

    # Extrahieren Sie Text aus dem PDF
    text = ''
    for page in reader.pages:
        text += page.extract_text()

    # Konvertieren Sie den Text in JSON
    data = json.dumps({'text': text})

    print(data)

client = OpenAI(
   api_key=os.getenv("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
  model="gpt-4-0125-preview",
  messages = [
    {"role": "system", "content": "Du bist ein Finanzassistent, der sich gut damit auskennt, Tabellen zu evaluieren und Berichte zu schreiben."},
    {"role": "user", "content": "Bitte überprüfe die folgende Daten und erstelle einen kurzen Bericht darüber: " + str(data)}
  ] 
)

print(completion.choices[0].message)