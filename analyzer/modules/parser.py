"""
analyzer/modules/parser.py
===========================
Responsibility: Read the uploaded file and extract structured data from the text.
"""

SKILL_KEYWORDS = [
    'python', 'javascript', 'java', 'c++', 'c#', 'react', 'django', 'node',
    'sql', 'html', 'css', 'aws', 'docker', 'git', 'machine learning',
    'data analysis', 'excel', 'photoshop', 'figma', 'flutter', 'kotlin',
    'typescript', 'mongodb', 'postgresql', 'linux', 'agile', 'scrum',
    'vue', 'angular', 'fastapi', 'flask', 'redis', 'kubernetes', 'terraform',
]

SECTION_KEYWORDS = {
    'has_contact':      ['email', 'phone', 'linkedin', 'github', '@'],
    'has_summary':      ['summary', 'objective', 'profile', 'about'],
    'has_education':    ['education', 'university', 'college', 'degree', 'bachelor', 'master', 'phd'],
    'has_experience':   ['experience', 'worked', 'job', 'position', 'role', 'company', 'intern'],
    'has_projects':     ['project', 'built', 'developed', 'created'],
    'has_achievements': ['achievement', 'award', 'honor', 'certificate', 'certified'],
}


def extract_text_from_pdf(file) -> str:
    """Try extracting PDF text using pypdf."""
    try:
        from pypdf import PdfReader
        file.seek(0)
        reader = PdfReader(file)
        pages_text = []
        for i, page in enumerate(reader.pages):
            t = page.extract_text()
            if t and t.strip():
                pages_text.append(t.strip())
        return ' '.join(pages_text).strip()
    except ImportError:
        return "__pdf_lib_missing__"
    except Exception as e:
        print(f"[parser] pypdf failed: {e}")
        return ""


def extract_text(file) -> str:
    """
    Read raw text from the uploaded file.
    Supports .pdf and .txt files.
    """
    filename = file.name.lower()
    print(f"[parser] File: {file.name} | Size: {file.size} bytes")

    # PDF
    if filename.endswith('.pdf'):
        result = extract_text_from_pdf(file)
        print(f"[parser] PDF extracted: {len(result)} chars")
        return result

    # TXT
    try:
        file.seek(0)
        content = file.read()
        text = content.decode('utf-8', errors='ignore') if isinstance(content, bytes) else str(content)
        print(f"[parser] TXT extracted: {len(text)} chars")
        return text
    except Exception as e:
        print(f"[parser] TXT failed: {e}")
        return ""


def parse_resume(text: str) -> dict:
    text_lower = text.lower()
    found_skills = [skill for skill in SKILL_KEYWORDS if skill in text_lower]
    sections = {
        key: any(word in text_lower for word in words)
        for key, words in SECTION_KEYWORDS.items()
    }
    return {
        'skills': found_skills,
        **sections,
        'word_count': len(text.split()),
        'char_count': len(text),
    }