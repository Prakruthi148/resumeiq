# 📄 ResumeIQ — AI-Powered Resume Analyzer

A Django web application that analyzes resumes and provides instant feedback, scoring, job role matches, and career path suggestions.

---

## 🚀 What It Does

Upload your resume and ResumeIQ will:

1. **Parse** — Extracts structured data from your resume (skills, experience, education)
2. **Score** — Gives your resume a score from 0–100 with a label (e.g. Strong, Average, Weak)
3. **Feedback** — Provides specific AI-generated suggestions to improve your resume
4. **Job Match** — Matches your skills to relevant job roles
5. **Career Path** — Suggests a career progression path based on your profile

---

## 🏗️ Project Structure

```
resumeiq/
│
├── analyzer/                    # Core ML/analysis logic
│   ├── modules/
│   │   ├── parser.py            # Extracts and parses resume text
│   │   ├── scorer.py            # Scores resume 0–100
│   │   ├── feedback.py          # Generates improvement feedback
│   │   ├── job_matcher.py       # Matches skills to job roles
│   │   └── career_advisor.py    # Suggests career path
│   ├── api/                     # API layer
│   └── service.py               # Orchestrates full analysis pipeline
│
├── frontend/                    # Django views + templates
│   ├── templates/
│   │   └── index.html           # Main single-page UI
│   ├── static/                  # CSS, JS assets
│   ├── views.py                 # Renders HTML pages
│   └── urls.py                  # URL routing
│
├── config/                      # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Layer       | Technology              |
|-------------|-------------------------|
| Backend     | Django 6.0              |
| PDF Parsing | pypdf                   |
| Frontend    | HTML, CSS, JavaScript   |
| Language    | Python 3.13             |

---

## 🛠️ Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Prakruthi148/resumeiq.git
cd resumeiq
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.

---

## 📋 How It Works — Pipeline

```
Upload Resume (PDF/TXT)
        ↓
   extract_text()        ← reads file content
        ↓
   parse_resume()        ← extracts skills, experience, education
        ↓
  calculate_score()      ← scores resume 0–100
        ↓
   get_feedback()        ← generates improvement suggestions
        ↓
  get_job_matches()      ← matches skills to job roles
        ↓
  get_career_path()      ← suggests career progression
        ↓
   Result displayed on UI
```

---

## 🎯 Key Design Decision

The `service.py` file is the **single orchestrator** — views never import individual modules directly. This keeps the architecture clean and modular. Each module has one responsibility:

- `parser.py` — only handles text extraction and parsing
- `scorer.py` — only handles scoring logic
- `feedback.py` — only handles feedback generation
- `job_matcher.py` — only handles job role matching
- `career_advisor.py` — only handles career suggestions

---

## 📬 API Usage

Send a POST request with a resume file:

```bash
curl -X POST http://127.0.0.1:8000/api/analyze/ \
  -F "resume=@your_resume.pdf"
```

**Response:**
```json
{
  "score": 78,
  "score_meta": { "label": "Strong", "color": "green" },
  "parsed": { "skills": ["Python", "Django", "SQL"], ... },
  "feedback": ["Add quantified achievements", "Include a summary section"],
  "job_matches": ["Backend Developer", "Data Engineer"],
  "career": { "current": "Junior Developer", "next": "Mid-level Engineer" }
}
```

---

## 👩‍💻 Author

Built by **Prakruthi** — targeting Data/ML Engineering roles in Bangalore.

Feel free to fork, star ⭐, and use as inspiration!
