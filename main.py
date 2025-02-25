import os
import pandas as pd
import PyPDF2
from drive import fetch_resumes, download_pdf
from rank import score_resume
from config import CSV_FILE_PATH, JOB_DESCRIPTION, CRITERIA_DEFINITIONS


# Extract text from a PDF file
def extract_text(file_id):
    pdf_stream = download_pdf(file_id)
    pdf_reader = PyPDF2.PdfReader(pdf_stream)
    text = " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return text


# Process resumes
def process_resumes():
    resumes = fetch_resumes()
    if not resumes:
        print("No resumes found in the Google Drive folder.")
        return []

    data = []
    for resume in resumes:
        try:
            print(f"Processing: {resume['name']}")
            resume_text = extract_text(resume["id"])
            scores = score_resume(JOB_DESCRIPTION, resume_text)
            if "total_score" not in scores:
                print(f"Skipping {resume['name']} due to missing score data.")
                continue

            data.append([resume["name"], resume["link"]] + [scores.get(key, 0) for key in CRITERIA_DEFINITIONS.keys()])
        except Exception as e:
            print(f"Error processing {resume['name']}: {e}")

    return data


# Ensure the 'data' directory exists before saving the CSV file
def ensure_directory_exists(file_path):
    csv_directory = os.path.dirname(file_path)
    if csv_directory and not os.path.exists(csv_directory):
        os.makedirs(csv_directory)


# Save results to CSV with Definitions
def save_results_to_csv(data):
    if not data:
        print("No data available to save.")
        return

    ensure_directory_exists(CSV_FILE_PATH)

    # Column headers using criteria from config
    columns = ["Candidate Name", "Resume Link"] + list(CRITERIA_DEFINITIONS.keys())

    df = pd.DataFrame(data, columns=columns)

    # Add criteria definitions as the first row
    definition_row = pd.DataFrame([["", ""] + list(CRITERIA_DEFINITIONS.values())], columns=columns)

    # Combine definition row and scores
    df_final = pd.concat([definition_row, df], ignore_index=True)

    # Save to CSV
    df_final.to_csv(CSV_FILE_PATH, index=False)
    print(f"Results saved in {CSV_FILE_PATH}")


if __name__ == "__main__":
    results = process_resumes()
    save_results_to_csv(results)





