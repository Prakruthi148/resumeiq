📄 ResumeIQ — AI-Powered Resume Analyzer
A Django web application that analyzes resumes and provides instant feedback, scoring, job role matches, and career path suggestions.
🚀 What It Does
Upload your resume and ResumeIQ will:
Parse — Extracts structured data from your resume (skills, experience, education)
Score — Gives your resume a score from 0–100 with a label (e.g. Strong, Average, Weak)
Feedback — Provides specific AI-generated suggestions to improve your resume
Job Match — Matches your skills to relevant job roles
Career Path — Suggests a career progression path based on your profile
🏗️ Project Structure
Code
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
⚙️ Tech Stack
Layer
Technology
Backend
Django 6.0
PDF Parsing
pypdf
Frontend
HTML, CSS, JavaScript
Language
Python 3.13
🛠️ Setup & Run Locally
1. Clone the repository
Bash
2. Create and activate virtual environment
Bash
3. Install dependencies
Bash
4. Run migrations
Bash
5. Start the server
Bash
Open http://127.0.0.1:8000 in your browser.
📋 How It Works — Pipeline
Code
🎯 Key Design Decision
The service.py file is the single orchestrator — views never import individual modules directly. This keeps the architecture clean and modular. Each module has one responsibility:
parser.py — only handles text extraction and parsing
scorer.py — only handles scoring logic
feedback.py — only handles feedback generation
job_matcher.py — only handles job role matching
career_advisor.py — only handles career suggestions
📬 API Usage
Send a POST request with a resume file:
Bash
Response:
Json
👩‍💻 Author
Built by Prakruthi — targeting Data/ML Engineering roles in Bangalore.
Feel free to fork, star ⭐, and use as inspiration!
