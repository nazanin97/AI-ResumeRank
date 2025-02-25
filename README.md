# AI-ResumeRank - AI-Powered Resume Scoring System

Resume Ranker is an AI-powered system that **automatically analyzes and ranks resumes** based on job-specific criteria. It fetches resumes from **Google Drive**, extracts text, scores candidates using **Google Gemini API**, and **saves the results in a CSV file** for easy review.

## 🚀 Features
✅ **Fetches resumes** from a Google Drive folder  
✅ **Extracts text** from PDF resumes  
✅ **Ranks candidates** using AI (Google Gemini API)  
✅ **Scores resumes based on multiple criteria** (Experience, Skills, Education, etc.)  
✅ **Saves results in CSV** with detailed scores and explanations  

---

## 🛠️ Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/resume-ranker.git
cd resume-ranker
```

### **2️⃣ Create a Virtual Environment (Optional)**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Google API Credentials**
- **Enable Google Drive API & Generate a Service Account JSON**  
- **Set up your Google Gemini API key**  
- **Update the `config.py` file with your credentials**:
```python
GOOGLE_API_KEY = "your_api_key"
CSV_FILE_PATH = "data/resumes.csv"

# Define criteria for scoring resumes
CRITERIA_DEFINITIONS = {
    "total_score": "Overall score based on all criteria (0-100)",
    "experience_score": "Years of relevant work experience in AI/ML (0-30)",
    "skills_score": "Technical skills match with job requirements (0-30)",
    "education_score": "Relevance of educational background (0-20)",
    "projects_score": "Quality and relevance of projects (0-10)",
    "communication_score": "Resume clarity and effectiveness (0-10)"
}

JOB_DESCRIPTION = "Looking for a Python Developer with AI/ML experience..."
```

---

## 🏃‍♂️ Usage

### **1️⃣ Run the Resume Ranking Process**
```sh
python main.py
```

### **2️⃣ Check the Results**
After execution, results will be saved in:
```
data/resumes.csv
```
The CSV file includes:
- Candidate names  
- Resume Google Drive links  
- Scores for each category  
- Explanation of each score  

---

## 📊 Example CSV Output

| Candidate Name | Resume Link | Total Score (0-100) | Experience (0-30) | Skills (0-30) | Education (0-20) | Projects (0-10) | Communication (0-10) |
|---------------|------------|----------------------|-------------------|--------------|----------------|---------------|----------------|
| John Doe | [Drive Link](https://drive.google.com/file/d/xyz) | 78 | 24 | 27 | 20 | 5 | 2 |
| Jane Smith | [Drive Link](https://drive.google.com/file/d/abc) | 45 | 15 | 21 | 18 | 0 | 10 |
| Mark Lee | [Drive Link](https://drive.google.com/file/d/lmn) | 70 | 20 | 80 | 80 | 60 | 70 |
