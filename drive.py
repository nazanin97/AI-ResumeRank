import os
import io
import json
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials
from config import SERVICE_ACCOUNT_FILE, GOOGLE_DRIVE_FOLDER_ID

# Authenticate with Google Drive API
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/drive"])
drive_service = build("drive", "v3", credentials=creds)


# List all PDF resumes in Google Drive folder
def list_pdfs():
    query = f"'{GOOGLE_DRIVE_FOLDER_ID}' in parents and mimeType='application/pdf'"
    results = drive_service.files().list(q=query).execute()
    return results.get("files", [])


# Download a PDF file
def download_pdf(file_id):
    request = drive_service.files().get_media(fileId=file_id)
    file_stream = io.BytesIO()
    downloader = MediaIoBaseDownload(file_stream, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()

    return file_stream


# Fetch resumes
def fetch_resumes():
    pdf_files = list_pdfs()
    return [{"name": file["name"], "id": file["id"], "link": f"https://drive.google.com/file/d/{file['id']}"} for file
            in pdf_files]
