import requests
import json
import config

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={config.GOOGLE_API_KEY}"

def score_resume(job_description, resume_text):
    # Generate criteria breakdown from config
    criteria_prompt = "\n".join([f"- {desc}" for desc in config.CRITERIA_DEFINITIONS.values()])

    prompt = f"""
    You are an expert recruiter. Given a job description and a candidate's resume, 
    score the resume based on the following criteria:

    {criteria_prompt}

    **Job Description:**
    {job_description}

    **Candidate Resume:**
    {resume_text}

    Provide only a **valid JSON object** without explanations, in the exact format:

    {{
        {", ".join([f'"{key}": <int>' for key in config.CRITERIA_DEFINITIONS.keys()])}
    }}

    Respond with JSON only, with no additional text or explanations.
    """

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(API_URL, json=payload, headers={"Content-Type": "application/json"})

    try:
        response_json = response.json()

        if response.status_code == 200 and "candidates" in response_json:
            ai_output = response_json["candidates"][0]["content"]["parts"][0]["text"]

            cleaned_json = ai_output.strip().replace("```json", "").replace("```", "").strip()
            scores = json.loads(cleaned_json)
            print(f"API Response: {scores}")

            return scores
        else:
            print("Short API Response: API Error")
            return {"error": f"Unexpected API response"}
    except Exception as e:
        print(f"Short API Response: Failed to parse response - {str(e)}")
        return {"error": f"Failed to parse API response: {str(e)}"}
